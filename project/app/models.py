from django.db import models

# Create your models here.
class Student(models.Model):
    Rollno = models.IntegerField()
    Name =  models.TextField()
    Age = models.IntegerField()
    Email = models.EmailField()
    Image = models.FileField()
    def __str__ (self):
        return self.Name