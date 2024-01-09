from django.shortcuts import render,redirect,HttpResponse
from .forms import UserRegistrationForm, OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Pizza, Order
from verify_email.email_handler import send_verification_email
from django. contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
import json
from baseApp.models import Pizza
from django.contrib.sites.shortcuts import get_current_site
from Marks_Pizzeria.settings import KEY_ID,KEY_SECRET
import razorpay
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from io import BytesIO
from Marks_Pizzeria import settings

from django.core.mail import EmailMultiAlternatives





# Create your views here.


razorpay_client= razorpay.Client(auth=(KEY_ID,KEY_SECRET))



def index(request):
    return render(request, "baseApp/index.html")


def about(request):    
    return render(request,'baseApp/about.html')



def menu(request):
    pizzas = Pizza.objects.all()
    pizza = Pizza.objects.first()
    return render(request, 'baseApp/order.html',{'pizzas':pizzas})



def signUp(request):
    context = {}
    form = UserRegistrationForm
    context["form"] = form
    if(request.method=="POST"):
        form = UserRegistrationForm(request.POST)
        if(form.is_valid()):
            inactive_user = send_verification_email(request, form)
            return redirect('login-page')
        
    
    return render(request,'baseApp/signUp.html',context = context)



def login(request):
    context=  {}
    # form = 
    return render(request,'baseApp/login.html')


def logoutView(request):
    logout(request)
    return redirect("home-page")

#for checkout and payment process
def checkout(request):
    if(request.method == "POST"):
        
        print('POST request executed')
        print(request.POST)
        order_items_json = json.loads(request.POST.get('order_items_json'))
        order_pizza_list = []
        order_total = 0
        for item in order_items_json:
            pizza_obj = Pizza.objects.get(id=item['id'])
            pizza_item = {
                "name":pizza_obj.name,
                "quantity":item['qty'],
                "price": item['qty']*item['price'],
                "image_url":pizza_obj.image_url
            }
            order_pizza_list.append(pizza_item)            
            order_total+= int(item['qty']) * item['price']
        print(order_pizza_list)
        print("Order total: ", order_total)
        #getting the order details
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        phone_number = request.POST.get('phone_number')
        
        
        try:
            usr_id =request.POST.get("user_id")
            usr = User.objects.get(id= usr_id)
            
        except:
            usr =None
            
        #creating a new order and giving it an order ID
        order = Order.objects.create(user = usr,first_name=first_name,last_name=last_name,street=street,city=city,state=state,zipcode= zipcode,phone_number= phone_number,order_amount=order_total*100,order_items = request.POST.get('order_items_json'))
        order.save()
        if usr is not None:
            print("The user is",usr)
        
        currency = 'INR'
        callback_URL = 'http://'+str(get_current_site(request))+'/handlerequest/'
        
        razorpay_order = razorpay_client.order.create(dict(amount=order_total*100, currency = currency,receipt = order.order_id))
        print(razorpay_order['id'])
        order.razorpay_order_id = razorpay_order['id']
        order.save()
        
        
        return render(request,"baseApp/paymentSummaryPage.html",{'order':order,'order_id':order.razorpay_order_id,'order_total':order_total,'KEY_ID':KEY_ID,"callback_URL":callback_URL,"order_pizza_list":order_pizza_list})

    
    return render(request, "baseApp/paymentSummaryPage.html",{})

@csrf_exempt
def cartView(request):
    prod_obj_arr = []
    total_price = 0
    form   = OrderForm()  
    
    
    
    if(request.method=='POST'):

        # return HttpResponse("success")
       
        cart_items_json = request.POST.get('cart_items_json')
        try:
            cart_items = json.loads(cart_items_json)
        except:
            cart_items = []     
        
        
        
        prods = []
        if(cart_items != None):
            
            for item in cart_items:

                prod_id = int(item.lstrip('pr'))
                pizza = Pizza.objects.get(id=prod_id)
                prods.append(pizza)
                

            
            prods = list(set(prods))
            for prod in prods:
                total_price+=prod.price
            
            return render(request,"baseApp/cart.html",{"prods":prods,"total_price":total_price,"form":form})

        
        
    print('printing from outside')
    return render(request,"baseApp/cart.html",{"prod_obj_arr":prod_obj_arr})



@csrf_exempt
def handlerequest(request):     
    
    if request.method=='POST':
        try:
            razorpay_order_id  = request.POST.get("razorpay_order_id","")
            razorpay_payment_id  = request.POST.get("razorpay_payment_id","")
            razorpay_signature  = request.POST.get("razorpay_signature","")
            
            order_db = Order.objects.get(razorpay_order_id = razorpay_order_id)
            order_db.razorpay_payment_id = razorpay_payment_id
            order_db.razorpay_signature = razorpay_signature
            order_db.paid = True
            order_db.save()
           
            order_items = json.loads(order_db.order_items)
            items= []
            for i in order_items:
                item_obj  ={
                    "name":Pizza.objects.get(id=i['id']).name,
                    "quantity":i['qty'],                    
                    "unit_price":Pizza.objects.get(id=i['id']).price,
                    "price":(i['price'] *i['qty'])
                }
                items.append(item_obj)
            
            
            try:
                to_email = order_db.user.email
            except:
                to_email = None
            
            if to_email is not None:
                
                pdf = render_to_pdf("baseApp/invoice.html",{"order":order_db,"items":items})             
                filename = "Invoice__"+order_db.order_id+".pdf"
                
                
                
                mail_subject = "Order Details!"
                email = EmailMultiAlternatives(
                            mail_subject,
                            "Hi, Thank you for ordering from Mark's Pizzeria!! ",       # necessary to pass some message here
                            settings.EMAIL_HOST_USER,
                            [to_email]
                        )
                email.attach(filename, pdf.getvalue(), 'application/pdf')
                email.send(fail_silently=False)   
     
            
           
            return render(request,"baseApp/paymentSuccess.html",{"order_id":order_db.order_id})
        except:
            
            return render(request,"baseApp/paymentFailure.html")
    
    
# For converting HTML data to PDF for things like invoice generation
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
    


# testing
    
def test_successPage(request):
    return render(request,"baseApp/paymentSuccess.html")
       
    
   
    

def test_failedPage(request):
    return render(request,"baseApp/paymentFailure.html")


def invoice_test(request):
    return render(request,"baseApp/invoice.html")








def invoice(request,id):   
    
    order = Order.objects.get(order_id=id)
    order_items = json.loads(order.order_items)
    items= []
    for i in order_items:
        item_obj  ={
            "name":Pizza.objects.get(id=i['id']).name,
            "quantity":i['qty'],
            "unit_price":Pizza.objects.get(id=i['id']).price,            
            "price":(i['price'] *i['qty'])
        }
        items.append(item_obj)
    
    pdf = render_to_pdf("baseApp/invoice.html",{"order":order,"items":items}) 
    
    
        
    return HttpResponse(pdf, content_type = "application/pdf")


    