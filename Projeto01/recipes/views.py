from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from utils.recipes.factory import make_recipe
from .models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

def category(request, category_id):
    # recipes = Recipe.objects.filter(category__id = category_id).order_by('-id')

    # recipes = get_list_or_404(Recipe.objects.filter(category__id = category_id).order_by('-id'), category_id = category_id, is_published = True)
    recipes = get_list_or_404(Recipe.objects.filter(category__id = category_id).order_by('id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': recipes[0].category.name
    })

def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    # recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/pages/recipe-viwe.html', context={
        'recipe': recipe,
        'is_datail_page': True,
    })

