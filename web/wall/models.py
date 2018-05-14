from django.db import models
class user(models.Model):
    user_name=models.CharField(max_length=16,default='user_name')
    passward=models.CharField(max_length=16,default='passward')
class message(models.Model):
    #message_date=models.CharField(max_length=100,default='0')
    message_content=models.TextField(null=False)
# Create your models here.
