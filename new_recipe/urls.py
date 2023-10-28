
from django.urls import path
from new_recipe import views

urlpatterns=[path("",views.home,name="home"),
              path("add_recipe/",views.add_recipe,name="add_recipe"),
              path("login_page/",views.login_page,name="login_page"),
              path("reg_page/",views.reg_page,name="reg_page"),
              path("logout_page/",views.logout_page,name="logout_page_page")
              ] 