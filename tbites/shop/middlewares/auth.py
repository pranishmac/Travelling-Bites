from django.shortcuts import redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        if not request.session.get('username'):
           return redirect('loginpage')
        else:
            response = get_response(request)
            return response

    return middleware