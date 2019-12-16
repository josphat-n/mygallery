from django.db import models

# Create your models here.
class Location(models.Model):
   location_name =  models.CharField(max_length =30)  
   
   def __str__(self):
      return self.location_name
   
   def save_location(self):
      self.save()   
   
class Category(models.Model):
   category_name =  models.CharField(max_length =30)   
   
class Image(models.Model):
   image_name = models.CharField(max_length =30)
   image_description = models.CharField(max_length =2000)
   image_location =models.ForeignKey(Location, on_delete=models.CASCADE,)
   image_category =models.ForeignKey(Category, on_delete=models.CASCADE,)
   image_image = models.ImageField(upload_to = 'img/',blank=True)

   