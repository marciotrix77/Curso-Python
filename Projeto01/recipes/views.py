from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

def category(request, category_id):
    recipes = Recipe.objects.filter(category__id = category_id).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
    })

def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/pages/recipe-viwe.html', context={
        'recipe': recipe,
        'is_datail_page': True,
    })

