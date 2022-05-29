
import email
from turtle import speed
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import RoundAndLevel, User,Store
from django.contrib.auth.hashers import make_password, check_password
import jwt
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
data = [
{"speed":200,"Round":1,"Level":1,"ImgSnake":"../../static/img/snakeredthom.png","Star": 0,"Background":"../../static/img/bg_12.jpg","icon":"../../static/img/thom.png"},
{"speed":150,"Round":1,"Level":2,"ImgSnake":"../../static/img/snakeredthom.png","Star": 0,"Background":"../../static/img/bg_12.jpg","icon":"../../static/img/thom.png"},
{"speed":120,"Round":1,"Level":3,"ImgSnake":"../../static/img/snakeredthom.png","Star": 0,"Background":"../../static/img/bg_12.jpg","icon":"../../static/img/thom.png"},
{"speed":100,"Round":2,"Level":1,"ImgSnake":"../../static/img/snakehongchanh.png","Star": 0,"Background":"../../static/img/bg_5.jpg","icon":"../../static/img/lemo.png"},
{"speed":90,"Round":2,"Level":2,"ImgSnake":"../../static/img/snakehongchanh.png","Star": 0,"Background":"../../static/img/bg_5.jpg","icon":"../../static/img/lemo.png"},
{"speed":80,"Round":2,"Level":3,"ImgSnake":"../../static/img/snakehongchanh.png","Star": 0,"Background":"../../static/img/bg_5.jpg","icon":"../../static/img/lemo.png"},
{"speed":60,"Round":3,"Level":1,"ImgSnake":"../../static/img/snakevangnho.png","Star": 0,"Background":"../../static/img/block.png","icon":"../../static/img/nho.png"},
{"speed":70,"Round":3,"Level":2,"ImgSnake":"../../static/img/snakevangnho.png","Star":0,"Background":"../../static/img/block.png","icon":"../../static/img/nho.png"},
{"speed":50,"Round":3,"Level":3,"ImgSnake":"../../static/img/snakevangnho.png","Star":0,"Background":"../../static/img/block.png","icon":"../../static/img/nho.png"}
]




def register(request):
    if request.method =='POST':
        emailCount = User.objects.filter(email=request.POST['email']).count()
        if(emailCount>0):
            return JsonResponse({'message': 'Email is ready !!!'})
        else:
            for round_data in list(data):
                round_create_data = RoundAndLevel.objects.create(speed=round_data['speed'],
                Round=round_data['Round'],
                Level= round_data['Level'],
                ImgSnake = round_data['ImgSnake'],
                Background = round_data['Background'],
                Star = 0,
                icon = round_data['icon'],
                email = request.POST['email']
                )
                round_create_data.save()
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
    token = request.COOKIES.get('token')
    round = request.POST['round']
    level = request.POST['level']
    try:
        payload = jwt.decode(jwt=token, key="secret", algorithms=['HS256'])
        user = User.objects.filter(email = payload['email']).values()
        if user:
            data = list(RoundAndLevel.objects.filter(Round=round,Level=level,email=payload['email']).values())[0]
            return JsonResponse({'data': data})
    except jwt.ExpiredSignatureError as e:
        return JsonResponse({'error': 'Activations link expired'}, status=400)
    except jwt.exceptions.DecodeError as e:
        return JsonResponse({'error': 'Invalid Token'}, status=400)
    

def UpdateMarkByRoundIDAndLevel(request):
    round = request.POST['round']
    level = request.POST['level']
    point = int(request.POST['point'])
    star = 0
    if point ==0:
        star = 0
    elif point >0 and point <=10:
        star =1
    elif point >10 and point <20:
        star = 2
    else:
        star = 3
    token = request.COOKIES.get('token')
    try:
        payload = jwt.decode(jwt=token, key="secret", algorithms=['HS256'])
        user = list(User.objects.filter(email = payload['email']).values())[0]
        roundData = list(RoundAndLevel.objects.filter(Round=round,Level=level,email=payload['email']).values())[0]
        if user:
            totalEat = point + user['totalEat']
            totalStar = star + user['totalStar']
            User.objects.filter(email=payload['email']).update(totalEat=totalEat,totalStar=totalStar)
            if(star > roundData['Star']):
                RoundAndLevel.objects.filter(Round=round,Level=level,email=payload['email']).update(Star=star)
            return JsonResponse({'message': totalEat,'star':totalStar}, status=200)
    except jwt.ExpiredSignatureError as e:
        return JsonResponse({'error': 'Activations link expired'}, status=400)
    except jwt.exceptions.DecodeError as e:
        return JsonResponse({'error': 'Invalid Token'}, status=400)

def getAllRoundAndStar(request):
    token = request.COOKIES.get('token')
    round = request.POST['round']
    try:
        payload = jwt.decode(jwt=token, key="secret", algorithms=['HS256'])
        user = User.objects.filter(email = payload['email']).values()
        if user:
            data = list(RoundAndLevel.objects.filter(Round=round,email=payload['email']).values())
            return JsonResponse({'data':data})
    except jwt.ExpiredSignatureError as e:
        return JsonResponse({'error': 'Activations link expired'}, status=400)
    except jwt.exceptions.DecodeError as e:
        return JsonResponse({'error': 'Invalid Token'}, status=400)
def getDataStore(request):
    data = list(Store.objects.filter().values())
    return JsonResponse({'data': data})

def gettopRank10(request):
    data = User.objects.all().order_by('totalStar').reverse().values()
    new = []
    for item in list(data)[0:5]:
        new.append({'nickname':item['nickname'],'star':item['totalStar']})
    return JsonResponse({'data':new})

def checkRound(request):
    token = request.COOKIES.get('token')
    round = request.POST['round']
    try:
        payload = jwt.decode(jwt=token, key="secret", algorithms=['HS256'])
        user = User.objects.filter(email = payload['email']).values()
        if user:
            dataCheck =list(RoundAndLevel.objects.filter(Round = round,email= payload['email']).values())
            valueStarRound = 0
            for el in dataCheck:
                if el['Star'] > 0:
                    valueStarRound +=1
            return JsonResponse({"data":valueStarRound})
    except jwt.ExpiredSignatureError as e:
        return JsonResponse({'error': 'Activations link expired'}, status=400)
    except jwt.exceptions.DecodeError as e:
        return JsonResponse({'error': 'Invalid Token'}, status=400)

