from django import forms
from .models import Student,employee,Course

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

class EmpForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'