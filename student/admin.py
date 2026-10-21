from django.contrib import admin
from .models import Course,Student,depart,employee

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(depart)
admin.site.register(employee)

