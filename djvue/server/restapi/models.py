from django.db import models
from django.db.models import Model
class Book(models.Model):
    title= models.CharField(max_length=200)  
    body= models.TextField(max_length=500)  


