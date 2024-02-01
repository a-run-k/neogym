from django.contrib import admin
from django.urls import path, include

from demo2app import views

urlpatterns = [
   path('',views.index,name='index'),

]
