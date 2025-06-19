from django.db import models


# Create your models here.
class student(models.Model):
    Rollno = models.IntegerField()
    Name =  models.TextField()
    Age = models.IntegerField()
    Email = models.EmailField()
    Image = models.FileField()
    
    def __str__ (self):
        return self.Name

class samplestudent(models.Model):
    roll = models.IntegerField()
    name = models.CharField()
    age = models.IntegerField()