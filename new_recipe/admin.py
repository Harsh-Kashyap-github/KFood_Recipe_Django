from django.contrib import admin
from new_recipe.models import recipe
from new_recipe.models import vegModel
# Register your models here.
admin.site.register(recipe)
admin.site.register(vegModel)