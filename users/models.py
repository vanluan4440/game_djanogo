from django.db import models

# Create your models here.
class User(models.Model):
  nickname = models.CharField(max_length=224, null=False, blank=False)
  email = models.EmailField(max_length=254, null=False, blank=False)
  password = models.CharField(max_length=255)
  scorce = models.IntegerField(default=0)
  star_store = models.IntegerField(default=0)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)