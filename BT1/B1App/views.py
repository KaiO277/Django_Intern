from django.shortcuts import render, redirect
from . models import  User
from django.http import HttpResponse

# Create your views here.

def index(request):
    users = User.objects.all()
    return render(request,  "B1App/index.html",{'users':users})

def insert(request):
    return render(request,  "B1App/insert.html")

def insertUser(request):
    username = request.POST['username']
    email = request.POST['email']
    address = request.POST['address']
    us = User(username = username, email=email, address=address)

    us.save()

    return redirect('/')

def deleteUser(request, pk):
    user_to_delete = User.objects.filter(id=pk)
    user_to_delete.delete()

    return redirect('/')

def update(requset, pk):

    user = User.objects.get(id=pk)

    return render(requset, "B1App/update.html",{'user':user})

def updateUser(request):

    user_id = request.POST.get('userId')
    user = User.objects.get(id=user_id)

    user.username = request.POST['username']
    user.email = request.POST['email']
    user.address = request.POST['address']

    user.save()

    return redirect('/')
