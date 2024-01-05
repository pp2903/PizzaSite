from django.urls import path
from . import views as base_views
from django.contrib.auth import views
urlpatterns = [
    
    path("",base_views.index,name="home-page"),
    path("about/",base_views.about,name="about-page"),
    path("order/",base_views.menu,name="menu-page"),
    path("signup/",base_views.signUp,name="signup-page"),
    path("login/",views.LoginView.as_view(template_name="baseApp/login.html"),name="login-page"),
    path("logout/",base_views.logoutView,name="logout-page"),
    path("checkout/",base_views.checkout,name="checkout-page"),
    path("cart/",base_views.cartView, name="cart-page"), 
    path('handlerequest/', base_views.handlerequest, name = 'handlerequest'),

]
