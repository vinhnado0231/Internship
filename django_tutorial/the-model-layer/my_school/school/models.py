from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

class Major(models.Model):
    name =  models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

    def get_enrollment_dates(self):
        # Lấy danh sách các ngày tham gia từ mô hình Enrollment
        return self.enrollment_set.values_list('date_joined', flat=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.major}"

    
    
class Class(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    students = models.ManyToManyField(Student, through="Enrollment")
    
    def get_students(self):
        return self.students.all()

    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    date_joined = models.DateField()


