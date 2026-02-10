from django.db import models

# Create your models here.
class Class(models.Model):
    stu_name = models.TextField()

    father_name = models.TextField()

class Driver(models.Model):
    name = models.TextField()
    license = models.TextField()

class Car(models.Model):
    car_name = models.TextField()
    model = models.TextField()
    year = models.IntegerField()
    owner = models.ForeignKey("Driver", on_delete=models.CASCADE)

class student(models.Model):
    stu_name = models.TextField()
    enr_num = models.IntegerField()
    course = models.TextField()
    sem = models.IntegerField()
    section = models.TextField()

class parent(models.Model):
    enr_num = models.IntegerField()
    stu_name = models.TextField()
    father_name = models.TextField()
    mother_name = models.TextField()
    add = models.TextField()
    ph_no = models.IntegerField()
    email = models.EmailField()
    owner = models.ForeignKey("student", on_delete=models.CASCADE)

class arun_info(models.Model):
    name = models.TextField()
    roll_no = models.IntegerField()
    reg_no = models.IntegerField()
    program = models.TextField()