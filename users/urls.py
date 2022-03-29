from . import views
from django.urls import path

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('update_password',views.forgot_password)
]
