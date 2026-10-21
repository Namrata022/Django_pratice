from django.db import models

# Create your models here.
class Course(models.Model):
    c_name=models.CharField(max_length=50)
    c_code=models.CharField(max_length=20,unique=True)
    start_date=models.DateField()
    end_date=models.DateField()
    faculty_name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.c_name

class Student(models.Model):
    name=models.CharField(max_length=100)
    c_name=models.ForeignKey(Course,on_delete=models.CASCADE,
                             null=True,blank=True
                             )
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    city=models.CharField(max_length=50)


    def __str__(self):
        return self.name

class depart(models.Model):
    depart_name=models.CharField(max_length=50)
    depart_code=models.CharField(max_length=50,unique=True)
    is_active=models.BooleanField(True)

    def __str__(self):
        return self.depart_name

class employee(models.Model):
    emp_id=models.CharField(max_length=50)
    emp_name=models.CharField(max_length=50)
    depart_name=models.ForeignKey(depart,on_delete=models.CASCADE,
                                  null=True,blank=True)
    email=models.EmailField(max_length=254)
    mobile=models.CharField()
    city=models.CharField(max_length=50)

    def __str__(self):
            return self.emp_name
