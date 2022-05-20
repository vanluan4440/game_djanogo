import email
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
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

def advanced(request):
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
        return render(request,template_name='advanced/index.html')
def game_advanced(request):
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
        return render(request,template_name='game_advanced/index.html')
def checkRound(request):
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
        data = list(User.objects.filter(email =payload['email']).values())[0]
        return JsonResponse({'data':data})
def updateRound(request):
    token = request.COOKIES.get('token')
    round = request.POST['round']
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
        if round == '1':
            User.objects.filter(email=payload['email']).update(Roud1=True)
        if round == '2':
            User.objects.filter(email=payload['email']).update(Roud2=True)
        if round == '3':
            User.objects.filter(email=payload['email']).update(Roud3=True)
        return JsonResponse({'message': 'succesfully'})
def gamePlayAdvanced(request):
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
        return render(request,template_name='levelGame/index.html')
def getTotal(request):
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
        data = list(User.objects.filter(email =payload['email']).values())[0]
        return JsonResponse({'data':data})


def store(request):
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
        return render(request,template_name='store/index.html')

def paid_snake(request):
    # token = request.COOKIES.get('token')
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imx1YW5AZ21haWwuY29tIn0.AtGLRlBgZZEEUJOqG-eSFUhbiXJUpP-4jMyZ9OMsq6M'
    apple = request.POST['apple']
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
        user_data = User.objects.filter(email =payload['email'] ).values()
        newValueEat = list(user_data)[0]['totalEat'] - int(apple)
        if newValueEat >0:
            User.objects.filter(email=payload['email']).update(totalEat=newValueEat)
            return JsonResponse({'message':'success'}) 
        else:
            return JsonResponse({'message':'payment failed'})
