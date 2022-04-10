import email
from django.shortcuts import redirect, render
from django.http import HttpResponse
import jwt

from users.models import User

# Create your views here.
def home(request):
    return render(request,template_name='home/index.html')
def register(request):
    return render(request,template_name='register/index.html')
def login(request):
    return render(request,template_name='login/index.html')
def forgot_password(request):
    return render(request,template_name='forgot_password/index.html')
def game(request):
    token = request.COOKIES.get('token')
    if not token:
        return redirect('/login')
    try:
        payload = jwt.decode(token,'secret',algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return redirect('/login')
    user = User.objects.filter(email =payload['email'] ).count()
    if user <1:
        return redirect('/login')
    else:
        return render(request,template_name='game/index.html')
def basic(request):
    token = request.COOKIES.get('token')
    if not token:
        return redirect('/login')
    try:
        payload = jwt.decode(token,'secret',algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return redirect('/login')
    user = User.objects.filter(email =payload['email'] ).count()
    if user <1:
        return redirect('/login')
    else:
        return render(request,template_name='basic/index.html')
