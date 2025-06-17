from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
    
class Task(models.Model):
    name= models.CharField(max_length=100)
    description= models.TextField(max_length=500)
    image= CloudinaryField('image',blank=True,null=True)
    dueDate= models.DateTimeField(null=True)
    is_complete=models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    is_priority = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    
    
    def __str__(self):
        return self.name

    
