
import re

from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Student,Cousre 


def home(request):
    # return HttpResponse("<h1 style='color:blue'>Hello, Welcome to Django</h1>")
    
    # data={
    #     'name':'Namrata',
    #     'course':'iMsc it',
    #     'college':'JGU'
    # }
    student_list=[
        'Namrata',
        'Nency',
        'Nenu'
    ]
    marks=20
    return render(request,'index.html',{'student':student_list,'marks':marks})

def contact(request,name):
    return HttpResponse("Contact Name :"+name)

def emp(request):
    emp=[
        {'name':'Namrata','salary':25000},
        {'name':'Nency','salary':300000}
    ]
    return render(request,'emp.html',{'employees':emp})


def stud_add(request):
    if request.method=="POST":
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            city=request.POST['city']
        )
        return redirect('list')

    return render(request,'stud_crud/add.html')

def stud_list(request):
    students=Student.objects.all()
    return render(request,'stud_crud/list.html',{'students':students})