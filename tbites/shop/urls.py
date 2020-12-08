from django.urls import path
from . import views
from shop.middlewares.auth import auth_middleware

urlpatterns = [
    # path("login", views.login, name="login"),
    path("home", auth_middleware(views.index), name="home"),
    path("menu/",auth_middleware(views.menu),name="menu"),
    path("menu/menu",auth_middleware(views.menu),name="menu"),
    path("menu/cart",auth_middleware(views.cart),name="cart"),
    path("",views.signup,name="signup"),
    path("verifymail",auth_middleware(views.verifymail),name="verifymail"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handleLogin, name="handleLogin"),
    path('loginpage', views.loginpage, name="loginpage"),
    path('logout', views.logout, name="logout"),
    path('error', views.error, name="error"),
    path('checkout', auth_middleware(views.checkout), name="checkout"),
    path('menu/myorders', auth_middleware(views.myorders), name="myorders"),
    path('myorders', auth_middleware(views.myorders), name="myorders"),
]