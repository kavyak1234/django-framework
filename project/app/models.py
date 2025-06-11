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

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=100,default='Snacks')
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name