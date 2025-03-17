import pytest
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
# @pytest.mark.fast 
class RecipeURLsTeste(TestCase):
    def test_the_pytest_is_ok(self):
        assert True

    def test_recipe_home_is_correct(self):
        url = reverse("recipes:home")
        self.assertEqual(url,'/')

    def test_recipe_category_is_correct(self):
        url = reverse("recipes:category", kwargs={'category_id': 1})
        self.assertEqual(url,'/recipes/category/1/')

        
    def test_recipe_detail_is_correct(self):
        url = reverse("recipes:recipe", kwargs={'id': 1})
        self.assertEqual(url,'/recipes/1/')

      