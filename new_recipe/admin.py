from django.contrib import admin
from new_recipe.models import recipe
from new_recipe.models import vegModel
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(recipe)
admin.site.register(vegModel)
