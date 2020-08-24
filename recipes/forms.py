from django import forms
from .models import CustomerRecipes


class AddRecipeForm(forms.ModelForm):

    class Meta:
        model = CustomerRecipes
        fields = ['name', 'description', 'ingredients', 'instructions', 'image', 'date_created', 'time_needed',
                  'level']
