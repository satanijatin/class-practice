from django.contrib import admin
from .models import Student
from .models import User


admin.site.register(User)

# Register your models here.
admin.site.register(Student)
