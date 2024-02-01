from django.contrib import admin
from django.urls import path, include

from cred import views

urlpatterns = [
   path('',views.index,name='index'),
   path('reg',views.reg,name='reg'),
   path('login',views.login,name='login'),
   path('logout',views.logout,name='logout'),

]
