from . import views
from django.urls import path

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('update_password',views.forgot_password),
    path('score',views.score),
    path('top10',views.gettop10),
    path('getRoundAndId', views.getRoundAndId),
    path('UpdateMarkByRoundIDAndLevel',views.UpdateMarkByRoundIDAndLevel),
    path('getAllRoundAndStar',views.getAllRoundAndStar)
]
