from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import redirect, render


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')

    return render(request,'login.html')
def reg(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username exists")
                return redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email exists")
                return redirect('reg')
            else:


                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save()
                return redirect('login')
            print("user created")
        else:
            messages.info(request,"password does not match")
    return render(request,"reg.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
def index(request):
  return  render(request,"index.html")