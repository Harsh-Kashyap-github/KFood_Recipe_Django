
from django.urls import path
from new_recipe import views

urlpatterns=[path("",views.home,name="home"),
              path("add_recipe/",views.add_recipe,name="add_recipe")
              ] 