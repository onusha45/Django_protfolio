from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('Savecontact/', Savecontact, name='Savecontact'),
]