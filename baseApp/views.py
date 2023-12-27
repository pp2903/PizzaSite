from django.shortcuts import render,redirect    
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Pizza
from verify_email.email_handler import send_verification_email
from django. contrib import messages

from django.contrib.auth import logout
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

@login_required
def checkout(request):
    pass





    