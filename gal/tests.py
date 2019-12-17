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