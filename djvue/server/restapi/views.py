"""from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializer import BookSerializer
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer"""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from datetime import datetime
import qrcode
from django.contrib import admin
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import keyboard
import ctypes
from datetime import timedelta
from datetime import date
from rest_framework import viewsets, filters, generics
from .models import *
from .serializer import *    


class AuthorViewSet(viewsets.ModelViewSet):
    search_fields = [ 'first_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

"""class AuthoriViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthoriSerializer"""

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class EditorViewSet(viewsets.ModelViewSet):
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    search_fields = ['isbn', 'book_name', ]
    filter_backends = (filters.SearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class VolumeViewSet(viewsets.ModelViewSet):
    search_fields = ['id']
    filter_backends = (filters.SearchFilter,)
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    def get_queryset(self, *args, **kwargs):
        queryset_list=Volume.objects.all()
        query= self.request.GET.get("isbn")
       # queryset = queryset.filter(workspace_id=workspace)
        if query:
            queryset_list= queryset_list.filter(book=query)
        return queryset_list

class LoanViewSet(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
    
    def get_queryset(self, *args, **kwargs):
        queryset_list=Loan.objects.all()
        query= self.request.GET.get("user")
       # queryset = queryset.filter(workspace_id=workspace)
        if query:
            queryset_list= queryset_list.filter(user_id=query)
        return queryset_list


"""class LoanList(generics.ListAPIView):
    serializer_class = LoanSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list=Loan.objects.all()
        query= request.GET.get("q")
        if query:
            queryset_list= queryset_list.filter(
                Loan(user=query)
            )
        return queryset_list
        
        class LoanViewSet(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
    
    def get_queryset(self, *args, **kwargs):
        queryset_list=Loan.objects.all()
        user = self.request.query_params.get('user')
        queryset = queryset.filter(user_id=user)
        if user:
            queryset_list= queryset_list.filter(user_id=q)
        return queryset_list
        """


