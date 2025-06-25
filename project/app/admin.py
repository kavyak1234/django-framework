from django.contrib import admin
from . models import student
from .models import posts


# Register your models here.
admin.site.register(student)
admin.site.register(posts)
