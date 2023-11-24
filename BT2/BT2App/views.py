from django.shortcuts import render, redirect
from .models import Person 

# Create your views here.

def index(request):
    persons = Person.objects.all()
    return render(request,'index.html',{'persons':persons})

def insert(request):
    return render(request, 'insert.html')

def insertPerson(request):
    username = request.POST['username']
    email = request.POST['email']
    address = request.POST['address']

    person = Person(username=username, email=email, address=address)
    person.save()

    return redirect('/')

def delete(request, pk):
    person = Person.objects.filter(id=pk)
    person.delete()

    return redirect('/')

def update(request, pk):
    person = Person.objects.get(id=pk)

    return render(request, 'update.html',{'person':person,'pk':pk})

def updatePerson(request, pk):
    person = Person.objects.get(id=pk)

    person.username = request.POST['username']
    person.email = request.POST['email']
    person.address = request.POST['address']

    person.save()

    return redirect('/')