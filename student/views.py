
import re

from django.shortcuts import get_object_or_404, render,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import(
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)


from .forms import CourseForm, StudentForm,EmpForm
from .models import Course, Student,depart,employee

@login_required(login_url='login')
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

@login_required(login_url='login')
def contact(request,name):
    return HttpResponse("Contact Name :"+name)

@login_required(login_url='login')
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
@login_required(login_url='login')
def stud_add(request):
    form=StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list')
    else:
        form=StudentForm()
    return render(request,'stud_crud/add.html',{'form':form})

@login_required(login_url='login')    
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

@login_required(login_url='login')
def stud_delete(request, id): 
    student = get_object_or_404(Student, id=id) 
    student.delete() 
    return redirect('list') 

@login_required(login_url='login')
def stud_list(request):
    students=Student.objects.all()
    return render(request,'stud_crud/list.html',{'students':students})

@login_required(login_url='login')
# employee FBV 
def emp_add(request):
    form=EmpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('Elist')
    else:
        form=EmpForm()
    return render(request,'emp_crud/add.html',{'form':form})

@login_required(login_url='login')
def emp_edit(request,id):
    emp=get_object_or_404(employee,id=id)
    if request.method == "POST":
        form=EmpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('Elist')
    else:
        form=EmpForm(instance=emp)
    return render(request,'emp_crud/edit.html',{'form':form,'employee':emp})

@login_required(login_url='login')
def emp_list(request):
    employees=employee.objects.all()
    return render(request,'emp_crud/list.html',{'employees':employees})

@login_required(login_url='login')
def emp_delete(request,id):
    emp = get_object_or_404(employee, id=id) 
    emp.delete() 
    return redirect('Elist')

@login_required(login_url='login')
# Session
def create_session(request):
    # create session
    request.session["name"]="Namrata"
    request.session["color"]="Blue"

    return redirect("home")

@login_required(login_url='login')
def show_session(request):

    # Read session
    name=request.session.get("name","No name")
    color=request.session.get("color","No color")

    return render(request,'session_show.html',{'name':name,'color':color})

@login_required(login_url='login')
def modify_session(request):
    # Modify session
    request.session["name"]="Nenu"
    request.session["color"]="Blue"

    return redirect("show_session")

@login_required(login_url='login')
def delete_session(request):
    # delete session
    request.session.flush()

    return redirect('home')

def login_view(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html',{
                'error':'Invalid username or password'
            })
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('login')

# CBV
class CourseCreateView(LoginRequiredMixin,CreateView):
    model=Course
    form_class=CourseForm
    template_name='course_crud/course_form.html'
    success_url=reverse_lazy('course_list')

class CourseListView(ListView):
    model=Course
    template_name='course_crud/course_list.html'
    context_object_name='courses'
    # search code
    def get_queryset(self):
        query=self.request.GET.get('q')
        if query:
            return Course.objects.filter(
                course_name_icontains=query
            )
        return Course.objects.all()

class CourseUpdateView(UpdateView):
    model=Course
    fields='__all__'
    template_name='course_crud/course_form.html'
    success_url=reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model=Course
    template_name='course_crud/course_conform_delete.html'
    success_url=reverse_lazy('course_list')

class CourseDetailView(DetailView):
    model=Course
    template_name='course_crud/course_detail.html'


# Ajax

#email checking ajax jquery 
def email_check_page(request): 
    return render(request,'email_check.html') 

def check_email(request):
    email=request.GET.get('email','')
    exists=Student.objects.filter(
        email__iexact=email
    ).exists()
    return JsonResponse({
        'available':not exists
    })
