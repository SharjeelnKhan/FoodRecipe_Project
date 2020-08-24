from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('popularrecipes/', views.popular_recipes, name='popularrecipes'),
    path('popularrecipes/<int:pk>/', views.popular_recipes_instructions, name='popular_recipes_instructions'),
    path('your_recipes/', views.your_recipes, name='your_recipes'),
    path('your_recipes_instructions/<int:pk>', views.your_recipe_instructions, name='your_recipes_instructions'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('update_recipe/<int:pk>/', views.update_recipe, name='update_recipe'),
    path('delete_recipe/<int:pk>/', views.delete_recipe, name='delete_recipe'),

]
