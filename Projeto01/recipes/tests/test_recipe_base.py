from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from recipes.models import Category, Recipe, User

# Create your tests here.
# @pytest.mark.fast 
class RecipeTesteBase(TestCase):

    def setUp(self):
        recipe = self.make_recipe()
        return super().setUp()

        
    def make_category(self, name='Category 1'):
        return Category.objects.create(name=name)
    
    def make_author(
            self, 
            first_name='Marcio', 
            last_name='Alencar',
            username='marcio.alencar2',
            password='123',
            email='marcio.alencar@gmail.com',
        ):
        return User.objects.create_user(
            last_name=last_name,
            first_name=first_name,
            username=username,
            password=password,
            email=email,
        )
    
    def make_recipe(
            self,
            title='Recipe 2',
            description='Description 2',
            slug='recipe-2',
            preparation_time=20,
            preparation_time_unit='minutes',
            servings=2,
            servings_unit='people',
            preparation_steps='Step 1, Step 2, Step 3',
            cover=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            category_data=None,
            author_data=None,
        ):

        if category_data is None:
            category = self.make_category()

        if author_data is None:
            author = self.make_author()

        return Recipe.objects.create(
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            cover=cover,
            category=category,
            author=author,
        )
    
