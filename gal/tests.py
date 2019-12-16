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