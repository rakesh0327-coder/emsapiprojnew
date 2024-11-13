from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token
    


# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)

def create_auth_token(sender, instance=None, created=False, **kwargs):
     if created:
          Token.objects.create(user=instance)

#create a department model class by inheriting the model class
class department(models.Model):
    #dept Id is auto incrementing and is primary key
    departmentId = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=200)

#whenever we try to print the dept objectz
#instead of the memory address of the object
#we need tom return the name of the department
    def __str__(self):
        return self.departmentName
    
class Employee(models.Model):
        EmployeeId = models.AutoField(primary_key=True)
        EmployeeName = models.CharField(max_length=200)
        Designation = models.CharField(max_length=150)
        DateOfJoining = models.DateField()
        departmentId = models.ForeignKey(department,on_delete=models.CASCADE)
        contact = models.CharField(max_length=150)
        IsActive = models.BooleanField(default=True)
        def __str__(self):
          return self.EmployeeName