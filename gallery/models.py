from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    categories = models.ManyToManyField(Category, related_name='images')
    created_date = models.DateField(default=timezone.now)
    age_limit = models.PositiveIntegerField()

    def __str__(self):
        return self.title
