import pytest
from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from django.core.files.uploadedfile import SimpleUploadedFile
from recipes.models import Category, Recipe, User
from .test_recipe_base import RecipeTesteBase

# Create your tests here.
# @pytest.mark.fast 
class RecipeViewTeste(RecipeTesteBase):
    def tearDown(self):
        return super().tearDown()

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse("recipes:category", kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_details_view_function_is_correct(self):
        view = resolve(reverse("recipes:recipe", kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def teste_recipe_home_view_returns_status_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def teste_recipe_home_view_returns_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def teste_recipe_home_tmplate_show_no_recipes_founds_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No Recipes Found.</h1>',
            response.content.decode('utf-8')
        )        

    def teste_recipe_category_view_returns_status_404_if_no_recipes(self):
        response = self.client.get(
            reverse("recipes:category", kwargs={'category_id': 10000})
        )
        self.assertEqual(response.status_code, 404)        

    def teste_recipe_detail_view_returns_status_404_if_no_recipes(self):
        response = self.client.get(
            reverse("recipes:recipe", kwargs={'id': 10000})
        )
        self.assertEqual(response.status_code, 404)          

    def teste_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        self.assertIn(self.recipe.title, content)
        self.assertIn(self.recipe.description, content)
        self.assertIn(self.recipe.category.name, content)
   
