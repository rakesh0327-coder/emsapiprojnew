from django.contrib import admin
from .models import department
from .models import Employee
from rest_framework.authtoken.models import Token
# Register your models here.
admin.site.register(department)
admin.site.register(Employee)
admin.site.register(Token)


