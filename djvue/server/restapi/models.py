
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Extra_user_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    document_type = models.CharField(max_length=50)
    document_number = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=10)

class Country (models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Editor(models.Model):
  name = models.CharField(max_length=50)
  country_id  = models.ForeignKey(Country, on_delete=models.CASCADE)

class Genre (models.Model):
  type =  models.CharField(max_length=50)
  def __str__(self):
        return self.type

class Author(models.Model):
    first_name =  models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    death_date = models.DateField()
    note = models.TextField()
    sex = models.TextChoices('Uomo', 'Donna')
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.last_name

class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=14 )
    book_name = models.CharField(max_length=200)
    book_plot = models.TextField()
    book_pages_number = models.IntegerField()
    book_release_date = models.DateField()
    book_language = models.CharField(max_length=50)
    book_image = models.CharField(max_length=500)
    author = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    
class Volume(models.Model):
    book_isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    dismission_date = models.DateField()

class  Prenotation(models.Model):
  date = models.DateTimeField(default=datetime.now)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  volume_id = models.ForeignKey(Volume, on_delete=models.CASCADE)

class Loan(models.Model):
  return_date = models.DateTimeField(default=datetime.now, blank=True)
  borrow_date = models.DateTimeField(default=datetime.now)
  user_id  = models.ForeignKey(User, on_delete=models.CASCADE)
  volume_id = models.ForeignKey(Volume, on_delete=models.CASCADE)    