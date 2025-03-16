import pytest
from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

# Create your tests here.
# @pytest.mark.fast 
class RecipeViewTeste(TestCase):
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

    def teste_recipe_category_view_returns_status_200(self):
        response = self.client.get(reverse("recipes:category", kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 200)

    def teste_recipe_home_tmplate_show_no_recipes_founds_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertContains(response, 'No recipes found')        