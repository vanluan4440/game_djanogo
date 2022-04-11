import email
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import User
from django.contrib.auth.hashers import make_password, check_password
import jwt
# Create your views here.

def register(request):
    if request.method =='POST':
        emailCount = User.objects.filter(email=request.POST['email']).count()
        if(emailCount>0):
            return JsonResponse({'message': 'Email is ready !!!'})
        else:
            user= User.objects.create(nickname=request.POST['username'],email=request.POST['email'],
            password = make_password(request.POST['password']), scorce = 0,star_store=0
            )
            user.save()
            return JsonResponse({'message': 'registed'})

    else:
        return JsonResponse({'message':'unauthorized'})
def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email']).values()
        if user:
            password = check_password(request.POST['password'],user[0]['password'])
            if password :
                payload = {'email' : request.POST['email']}
                token = jwt.encode(payload,"secret", algorithm="HS256")
                return JsonResponse({'token': token})
            else:
                return JsonResponse({'message': 'wrong password'})
        else:
            return JsonResponse({'message':'wrong email'})
    else:
        return JsonResponse({'message':'unauthorized'}) 
def forgot_password(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email']).update(password= make_password(request.POST['password']))
        if user:
            return JsonResponse({'message':'Update password'})
        else:
            return JsonResponse({'message':'Email not match'})
