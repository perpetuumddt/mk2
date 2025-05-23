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

    #testing category creation
    def test_category_creation(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(str(self.category), "Test Category")
    #testing category name max length
    def test_category_name_max_length(self):
        max_length = self.category._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

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

    # testing image creation with proper attributes
    def test_image_creation(self):
        self.assertTrue(isinstance(self.image, Image))
        self.assertEqual(self.image.title, "Test Image")
        self.assertEqual(self.image.age_limit, 18)
        self.assertEqual(str(self.image), "Test Image")

    # testing image fields
    def test_image_fields(self):
        self.assertEqual(self.image._meta.get_field('title').max_length, 200)
        self.assertEqual(self.image.categories.count(), 1)
        self.assertEqual(self.image.categories.first(), self.category)
        self.assertEqual(self.image.created_date, timezone.now().date())
        self.assertTrue(self.image.age_limit > 0)

    # testing image categories relationship
    def test_image_categories_relationship(self):
        category2 = Category.objects.create(name="Test Category 2")

        self.image.categories.add(category2)

        self.assertEqual(self.image.categories.count(), 2)
        self.assertIn(category2, self.image.categories.all())

    # deleting test image file
    def tearDown(self):
        if self.image.image:
            if os.path.isfile(self.image.image.path):
                os.remove(self.image.image.path)
