from msilib.schema import Class
from django.db import models

# Create your models here.
class User(models.Model):
  nickname = models.CharField(max_length=224, null=False, blank=False)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=255)
  scorce = models.IntegerField(default=0)
  star_store = models.IntegerField(default=0)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  totalStar = models.IntegerField(default=0)
  totalEat = models.IntegerField(default=0)
  Roud1 = models.BooleanField(default=False)
  Roud2 = models.BooleanField(default=False)
  Roud3 = models.BooleanField(default=False)

class StarOnRound(models.Model):
  userid = models.IntegerField(default=0)
  Round = models.IntegerField(default=0)
  Level = models.IntegerField(default=0)
  Star = models.IntegerField(default=0)

class RoundAndLevel(models.Model):
  speed = models.IntegerField(default=0)
  Round = models.IntegerField(default=0)
  Level = models.IntegerField(default=0)
  ImgSnake = models.CharField(max_length=255)
  Background = models.CharField(max_length=255, default='')
  Star = models.IntegerField(default=0)
  icon = models.CharField(default='', max_length=255)


    