from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    slug = models.SlugField(max_length=300)
    author = models.ManyToManyField(User)
    pages = models.IntegerField()
    date_published = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="book_images", blank=True, null=True)

    def __str__(self):
        return self.title
