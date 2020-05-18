from django.contrib import admin
from .models import Extra_user_info, Country, Editor, Genre, Author, Book, Volume, Prenotation,Loan 
admin.site.register(Author)
admin.site.register(Extra_user_info)
admin.site.register(Country)
admin.site.register(Editor)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Volume)
admin.site.register(Prenotation)
admin.site.register(Loan)
