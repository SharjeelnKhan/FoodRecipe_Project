from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CustomerRecipes(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField('2020-8-17', null=True, blank=True)
    time_needed = models.CharField(max_length=25, blank=True)
    level = models.CharField(max_length=25, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class PopularRecipes(models.Model):
    name = models.CharField(max_length=50, null=True, default=True)
    description = models.CharField(max_length=100, null=True, default=True)
    ingredients = models.TextField(default=True)
    instructions = models.TextField(default=True)
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField('2020-8-17')
    time_needed = models.CharField(max_length=25, default=True)
    level = models.CharField(max_length=25, default=True)

    def __str__(self):
        return self.name


class GalleryRecipe(models.Model):
    name = models.CharField(max_length=50, null=True, default=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name



