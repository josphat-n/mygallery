from django.db import models

# Create your models here.
class Location(models.Model):
   location_name =  models.CharField(max_length =30)  
   
   def __str__(self):
      return self.location_name
   
   def save_location(self):
      """
      This function describes how a new location is saved
      """
      self.save() 
       
   @classmethod
   def get_location(cls,location):
      """
      function to get location a querried location
      """
      location=cls.objects.filter(location_name=location)
      return location 
   
   def delete_location(self):
      """
      Delete a location from the database
      """
      self.delete()
   
class Category(models.Model):
   """
   This class defines the various categories of the images
   """
   category_name =  models.CharField(max_length =30)   
   
   def __str__(self):
      return self.category_name
   
   def save_category(self):
      """
      function to save a category to the database
      """
      self.save()  
      
   def delete_category(self):
      """
      function to delete a category from the database
      """
      self.delete() 
      
   @classmethod
   def search_category(cls,category):
      """
      function to querry the category table and returns the category name according to the search criteria
      """
      category=cls.objects.filter(category_name=category)
      return category       
      
class Image(models.Model):
   image_name = models.CharField(max_length =30)
   image_description = models.TextField()
   image_location =models.ForeignKey(Location, on_delete=models.CASCADE,)
   image_category =models.ForeignKey(Category, on_delete=models.CASCADE,)
   image_image = models.ImageField(upload_to = 'img/',blank=True)
   
   def __str__(self):
      return self.image_name
   
   class Meta:
      ordering=['image_name'] 
      
   @classmethod
   def get_all(cls):
      """
      This function allows for the fetching of all the image objects from the database
      """
      imgs = Image.objects.all()
      return imgs  
   
   def save_image(self):
      """
      Save a new image to the database    
      """
      self.save()  
   
   def delete_image(self):
      """
      function to delete an image from the db
      """
      self.delete()  
    
   def search_image(category):
      """
      function for searching for an image by Category
      """
      category=Category.objects.filter(category_name = 'search_term')
      imgs =Image.objects.filter(image_category=category)
      
   @classmethod
   def get_image_by_id(cls,image_id):
      """
      function to search an image by id
      """
      img =cls.objects.filter(id=image_id)
      return img
      
   @classmethod
   def get_images_by_location(cls,location_name):
      """
      function to get images of the same location
      """
      imgs =cls.objects.filter(location__in=location_name) 
      return imgs  