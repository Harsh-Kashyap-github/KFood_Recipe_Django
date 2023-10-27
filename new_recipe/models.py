from django.db import models

# Create your models here.
class recipe(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(null=True,blank=True,upload_to="")
    op=models.CharField(max_length=10)
    desc=models.CharField(max_length=10000)
    
    def __str__(self):
        return self.name

class vegModel(models.Model):
    isVeg=models.BooleanField(default=False)
    