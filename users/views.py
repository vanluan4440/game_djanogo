
import email
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import RoundAndLevel, User
from django.contrib.auth.hashers import make_password, check_password
import jwt
from django.core.mail import send_mail
from django.conf import settings
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
            subject = '[CHANGE PASSWORD]'
            message = 'new password is {}'.format(request.POST['password'])
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email']]
            send_mail( subject, message, email_from, recipient_list )
            return JsonResponse({'message':'Update password'})
        else:
            return JsonResponse({'message':'Email not match'})
def score(request):
    score = request.POST['score']
    token = request.COOKIES.get('token')
    try:
        payload = jwt.decode(jwt=token, key="secret", algorithms=['HS256'])
        user = User.objects.filter(email = payload['email']).values()
        if user:
            if int(score) > int(user[0]['scorce']):
                User.objects.filter(email = payload['email']).update(scorce=score)
            return JsonResponse({'message': 'Successfully'}, status=200)
    except jwt.ExpiredSignatureError as e:
        return JsonResponse({'error': 'Activations link expired'}, status=400)
    except jwt.exceptions.DecodeError as e:
        return JsonResponse({'error': 'Invalid Token'}, status=400)

def gettop10(request):
    data = User.objects.all().order_by('scorce').reverse().values()
    new = []
    for item in list(data)[0:10]:
        new.append({'nickname':item['nickname'],'score':item['scorce']})
    return JsonResponse({'data':new})

def getRoundAndId(request):
    round = request.POST['round']
    level = request.POST['level']
    data = list(RoundAndLevel.objects.filter(Round=round,Level=level).values())[0]
    return JsonResponse({'data': data})

def UpdateMarkByRoundIDAndLevel(request):
    round = request.POST['round']
    level = request.POST['level']
    point = int(request.POST['point'])
    star = 0
    if point <=10:
        star = 1
    elif point >10 and point <20:
        star = 2
    else:
        star = 3
    token = request.COOKIES.get('token')
    try:
        payload = jwt.decode(jwt=token, key="secret", algorithms=['HS256'])
        user = list(User.objects.filter(email = payload['email']).values())[0]
        roundData = list(RoundAndLevel.objects.filter(Round=round,Level=level).values())[0]
        if user:
            totalEat = point + user['totalEat']
            totalStar = star + user['totalStar']
            User.objects.filter(email=payload['email']).update(totalEat=totalEat,totalStar=totalStar)
            if(star > roundData['Star']):
                RoundAndLevel.objects.filter(Round=round,Level=level).update(Star=star)
            return JsonResponse({'message': totalEat,'star':totalStar}, status=200)
    except jwt.ExpiredSignatureError as e:
        return JsonResponse({'error': 'Activations link expired'}, status=400)
    except jwt.exceptions.DecodeError as e:
        return JsonResponse({'error': 'Invalid Token'}, status=400)

def getAllRoundAndStar(request):
    round = request.POST['round']
    data = list(RoundAndLevel.objects.filter(Round=round).values())
    return JsonResponse({'data':data})
    

