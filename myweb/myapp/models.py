from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.CharField(max_length=20)
    message=models.TextField()
    connect=models.ForeignKey( User,on_delete=models.CASCADE,null=True)