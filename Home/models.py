from django.db import models

# Create your models here.
class Vegetables(models.Model):
    image = models.ImageField(upload_to='static/image/',null=True, blank=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.FloatField()
    description = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
    

    
    
class Fruits(models.Model):
     image = models.ImageField(upload_to='static/image/',null=True,blank=True)
     name =models.CharField(max_length=50)
     quantity = models.FloatField()
     price = models.IntegerField()
     description = models.CharField(max_length=100)
     
     
     def __str__(self):
         return self.name   