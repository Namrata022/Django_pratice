
import re

from django.shortcuts import get_object_or_404, render,redirect

# Create your views here.
from django.http import HttpResponse

from .forms import StudentForm
from .models import Course, Student


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


# def stud_add(request):
#     if request.method=="POST":
#         Student.objects.create(
#             name=request.POST['name'],
#             email=request.POST['email'],
#             mobile=request.POST['mobile'],
#             city=request.POST['city']
#         )
#         return redirect('list')

#     return render(request,'stud_crud/add.html')
def stud_add(request):
    form=StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list')
    else:
        form=StudentForm()
    return render(request,'stud_crud/add.html',{'form':form})
    

# 
def stud_edit(request,id):
    student=get_object_or_404(Student, id=id)
    if request.method == "POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form=StudentForm(instance=student)
    return render(request,'stud_crud/edit.html',{
        'form':form,
        'student':student})

def stud_delete(request, id): 
    student = get_object_or_404(Student, id=id) 
    student.delete() 
    return redirect('list') 

def stud_list(request):
    students=Student.objects.all()
    return render(request,'stud_crud/list.html',{'students':students})


# Session
def create_session(request):
    # create session
    request.session["name"]="Namrata"
    request.session["color"]="Blue"

    return redirect("home")

def show_session(request):

    # Read session
    name=request.session.get("name","No name")
    color=request.session.get("color","No color")

    return render(request,'session_show.html',{'name':name,'color':color})

def modify_session(request):
    # Modify session
    request.session["name"]="Nenu"
    request.session["color"]="Blue"

    return redirect("show_session")

def delete_session(request):
    # delete session
    request.session.flush()

    return redirect('home')
