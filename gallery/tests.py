from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from .models import Category, Image
import os

#testing category model
class CategoryModelTest(TestCase):
    #setting up test category
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")


#testing image model
class ImageModelTest(TestCase):
    #setting up test image
    def setUp(self):
        # Create test category
        self.category = Category.objects.create(name="Test Category")
        
        # Create test image file
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )
        
        # Create test image object
        self.image = Image.objects.create(
            title="Test Image",
            image=self.test_image,
            created_date=timezone.now().date(),
            age_limit=18
        )
        self.image.categories.add(self.category)

