from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from .filters import *
# Create your views here.


@login_required
def home(request):
    return render(request, 'recipes/dashboard.html')


def gallery(request):
    recipes = GalleryRecipe.objects.all()

    context = {'recipes': recipes}
    return render(request, 'recipes/gallery.html', context)


def popular_recipes(request):
    recipes = PopularRecipes.objects.all()
    popular_recipes_filter = PopularRecipeFilter(request.GET, queryset=recipes)
    recipes = popular_recipes_filter.qs

    context = {'recipes': recipes, 'popular_recipes_filter': popular_recipes_filter}
    return render(request, 'recipes/popularrecipes.html', context)


def popular_recipes_instructions(request, pk):
    recipes = get_object_or_404(PopularRecipes, id=pk)
    # allrecipes = PopularRecipes.objects.all()

    context = {'recipes': recipes}  # 'allrecipes': allrecipes}
    return render(request, 'recipes/popular_recipes_instructions.html', context)


def your_recipes(request):
    recipes = CustomerRecipes.objects.all()
    myfilter = RecipeFilter(request.GET, queryset=recipes)
    recipes = myfilter.qs

    context = {'recipes': recipes, 'myfilter': myfilter}
    return render(request, 'recipes/your_recipes.html', context)


def your_recipe_instructions(request, pk):
    recipes = get_object_or_404(CustomerRecipes, id=pk)

    context = {'recipes': recipes}
    return render(request, 'recipes/your_recipes_instructions.html', context)


def add_recipe(request):
    form = AddRecipeForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

        return redirect('your_recipes')

    context = {'form': form}
    return render(request, 'recipes/add_recipe.html', context)


def update_recipe(request, pk):
    updaterecipe = CustomerRecipes.objects.get(id=pk)
    form = AddRecipeForm(instance=updaterecipe)

    if request.method == 'POST':
        form = AddRecipeForm(request.POST, instance=updaterecipe)
        if form.is_valid():
            form.save()
            return redirect('your_recipes')

    context = {'form': form}
    return render(request, 'recipes/update_recipe.html', context)


def delete_recipe(request, pk):
    recipe = CustomerRecipes.objects.get(id=pk)

    if request.method == 'POST':
        recipe.delete()
        return redirect('your_recipes')

    context = {'recipe': recipe}
    return render(request, 'recipes/delete_recipe.html', context)

