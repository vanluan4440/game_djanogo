from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def user(request):
    return HttpResponse('api user', status=200)
