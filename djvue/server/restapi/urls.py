from django.urls import path, include
from django.contrib import admin
from . import views
from restapi.views import *
urlpatterns = [
    
    path('admin/loan/', views.loan_modifier, name='loan_modifier'),
]
