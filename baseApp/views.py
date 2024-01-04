from django.shortcuts import render,redirect,HttpResponse
from .forms import UserRegistrationForm, OrderForm
from django.contrib.auth.decorators import login_required
from .models import Pizza
from verify_email.email_handler import send_verification_email
from django. contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
import json
from baseApp.models import Pizza
# Create your views here.






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


def checkout(request):
    if(request.method == "POST"):
        print('POST request executed')
        print(request.POST)
        order_items_json = json.loads(request.POST.get('order_items_json'))
        print(order_items_json)
        order_total = 0
        for item in order_items_json:
            order_total+= int(item['qty']) * item['price']
        print("Order total: ", order_total)
        return redirect('home-page')


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




    
    # we will process the order here   
    
      
    
    
    



    