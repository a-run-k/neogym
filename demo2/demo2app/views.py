from django.http import HttpResponse
from django.shortcuts import render
from .models import  Demo2app


# Create your views here.
def index(request):
  obj=Demo2app.objects.all()
  return  render(request,"index.html",{'re':obj})





