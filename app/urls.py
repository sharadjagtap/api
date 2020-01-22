from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('email/',views.email, name='email'),
    path('time/',views.time,name='time')
]
