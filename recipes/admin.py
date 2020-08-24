from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CustomerRecipes)
admin.site.register(PopularRecipes)
admin.site.register(GalleryRecipe)
