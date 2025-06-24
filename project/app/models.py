from django.db import models
from django.contrib.auth.models import User

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

class posts(models.Model):
    title = models.TextField()
    tags = models.TextField()
    file = models.FileField()
    date = models.DateField()
    user_dtls = models.ForeignKey(User,on_delete=models.CASCADE)

class commends(models.Model):
    text = models.TextField()
    user_dtls = models.ForeignKey(User,on_delete=models.CASCADE)
    post_dtls =models.ForeignKey(posts,on_delete=models.CASCADE)


