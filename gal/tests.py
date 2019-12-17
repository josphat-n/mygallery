from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestClass(TestCase):   
   # Set up method
   def setUp(self):
      self.nairobi= Location(location_name = 'Nairobi')
   
   # Testing  instance
   def test_instance(self):
      self.assertTrue(isinstance(self.nairobi,Location))  
          
   # Testing Save Method
   def test_save_method(self):
      self.nairobi.save_location()
      locations = Location.objects.all()
      self.assertTrue(len(locations) > 0)  
       
   # Testing Delete Method
   def test_delete(self):
      self.nairobi.save_location()
      self.nairobi.delete_location()
      locations =Location.objects.all()
      self.assertTrue(len(locations)<1)
      
   # Testing get_location Method
   def test_get_location(self):
      self.nairobi.save_location()
      found_location=Location.get_location('nairobi')
      self.assertEquals(len(found_location),1)
   
   # Test the functionality to delete all objects
   def tearDown(self):
      Location.objects.all().delete()
      
class CategoryTestClass(TestCase):
   # Set up method
   def setUp(self):
      self.food= Category(category_name = 'food')
   
   # Testing  instance
   def test_instance(self):
      self.assertTrue(isinstance(self.food,Category))  
          
   # Testing Save Method
   def test_save_method(self):
      self.food.save_category()
      categories = Category.objects.all()
      self.assertTrue(len(categories) > 0)  
      
   # Teardown Method
   def tearDown(self):
      Category.objects.all().delete()
   
   #Delete Method   
   def test_delete(self):
      self.food.save_category()    
      self.food.delete_category()
      categories=Category.objects.all()
      self.assertTrue(len(categories)<1)    
    
   #Search Functionality
   def test_get_category(self):
      self.food.save_category()
      foods =Category.search_category('foods')
      self.assertEquals(len(foods),1) 
      
class ImageTestClass(TestCase):      
   # Setup Method
   def setUp(self):
      self.location=Location(name='Nakuru')
      self.Category=Category(name='food')
      self.image_one=Image(image_name='ted',image_description='A classical commical movie',)
   
   # Testing Instance
   def test_instance(self):
      self.assertTrue(isinstance(self.image_one,Image)) 
   
   # Testing Save Method
   def test_save_method(self):
      self.image_one.save_image()
      imgs = Image.objects.all()
      self.assertTrue(len(imgs) > 0)   
   
   # Teardown Method
   def tearDown(self):
      Image.objects.all().delete()    
   
   #Delete Method   
   def test_delete(self):
      self.image_one.save_image()    
      self.image_one.delete_image()
      imgs=Image.objects.all()
      self.assertTrue(len(imgs)<1) 
         
   #Get_image_by_id
   def test_get_image_by_id(self):
      self.image_one.save_image() 
         
      try:
         found=Image.get_image_by_id(self.image1.id)      
      
      except ValueError:
         raise AttributeError
      
      self.assertEquals(len(found),1)
   
   #Test Search   
   def test_search_image(self):
      self.image_one.save_image() 
      search_term= 'food'
      reslt =Category.objects.filter(category_name = 'search_term')
      imgs =Image.objects.filter(image_category=reslt)

   #Test get_images_by_location
   def test_get_images_by_location(self):
      self.image_one.save_image() 
      search_term = 'Nakuru'
      loc=Location.get_location(search_term)
      result=Image.get_images_by_location(loc)
      
      self.assertEquals(len(result),1)