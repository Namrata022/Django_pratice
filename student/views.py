
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.http import HttpResponse
from .models import Cousre, Student


def home(request):
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
    courses = Cousre.objects.all()
    if request.method=="POST":
        course_id = request.POST.get('c_name')
        Student.objects.create(
            name=request.POST['name'],
            c_name=get_object_or_404(Cousre, pk=course_id) if course_id else None,
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            city=request.POST['city']
        )
        return redirect('list')

    return render(request, 'stud_crud/add.html', {'course': courses})

def stud_edit(request, id):
    student = get_object_or_404(Student, pk=id)
    courses = Cousre.objects.all()
    if request.method=="POST":
        course_id = request.POST.get('c_name')
        student.name = request.POST['name']
        student.c_name = get_object_or_404(Cousre, pk=course_id) if course_id else None
        student.email = request.POST['email']
        student.mobile = request.POST['mobile']
        student.city = request.POST['city']
        student.save()
        return redirect('list')

    return render(request, 'stud_crud/edit.html', {
         'student': student,
         'course': courses,
    })

def stud_delete(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return redirect('list')

def stud_list(request):
    students=Student.objects.all()
    return render(request,'stud_crud/list.html',{'students':students})