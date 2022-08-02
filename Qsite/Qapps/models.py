from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models
from django.contrib.auth.models import User
#3rd apps field

# Create your models here.

class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=200)
    objects = models.Manager()

class Replys(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    rep = models.TextField()
    author_rep = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()