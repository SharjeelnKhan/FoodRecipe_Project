import django_filters
from .models import *


class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model = CustomerRecipes
        fields = ['name', 'level']


class PopularRecipeFilter(django_filters.FilterSet):
    class Meta:
        model = PopularRecipes
        fields = ['name']
