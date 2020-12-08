from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from .models import item
from .models import order
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from shop.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

def index(request):
    print(request.session.get('username'))
    return render(request,"shop/index.html")

def menu(request):
    if request.method=="POST":
        prod = request.POST.get('prod')
        remove = request.POST.get('remove')
        # print(prod) 
        cart = request.session.get('cart')
        if cart:
            cart={}
            cart = request.session.get('cart')
            quantity = cart.get(prod)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(prod)
                    else:
                        cart[prod] = quantity-1
                else:
                    cart[prod]= quantity+1

            else:
                cart[prod] = 1
        else:
            cart = {}
            cart[prod] = 1
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        
        return redirect('menu')

    else:
     items= item.objects.all()
    #  print(items)
     n=len(items)
     param={'items':items}
     return render(request,"shop/menu_page.html",param)
    

def signup(request):
    return render(request,"shop/Registeration_page.html")

def cart(request):
    ids = list(request.session.get('cart').keys())
    print(ids)
    products = item.get_products_by_id(ids)
    print(products)
    return render(request,"shop/cart.html", {'products' : products})


def checkout(request):
    if request.method=="POST":
        username = request.POST.get('username')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        cart = request.session.get('cart')
        products = item.get_products_by_id(list(cart.keys()))
        print(address, phone,cart, products)

        for product in products:
            print(cart.get(str(item.id)))
            Order = order(item=product,
                          price=product.price,
                          username=username,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            Order.save()
        request.session['cart'] = {}

        return redirect('cart')

def myorders(request):
    customer=request.session.get('username')
    print(customer)
    orders= order.get_orders_by_customer(customer)
    print(orders)
    return render(request,'shop/orders.html', {'orders' : orders})


def loginpage(request):
    return render(request,"shop/Login_Page.html")

def verifymail(request):
    return render(request,"shop/email_verification.html")
def error(request):
    return render(request,"shop/error.html")

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('error')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('error')

        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('error')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('loginpage')

    else:
        return HttpResponse("404 - Not found")


def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:

            login(request, user)
            request.session['user_id'] = user.id 
            request.session['username'] = user.username 
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('error')

    return HttpResponse("404- Not found")
   

    # return HttpResponse("login")

def logout(request):
    request.session.clear()
    return render(request,'shop/Login_Page.html')
