from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login',views.login,name='login'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('game',views.game,name='game')
]
