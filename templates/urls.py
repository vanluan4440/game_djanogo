from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login',views.login,name='login'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('game',views.game,name='game'),
    path('basic',views.basic,name='basic'),
    path('advanced',views.advanced,name='advanced'),
    path('game_advanced',views.game_advanced,name='game_advanced'),
    path('checkRound',views.checkRound,name="checkRound"),
    path('updateRound',views.updateRound,name="updateRound")
]
