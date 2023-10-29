from django.shortcuts import render,redirect
from new_recipe.models import recipe

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

global_user=""
# Create your views here.
def home(response):
    r1=recipe.objects.all()       
    variable={"recipes":r1}
    return render(response,"new_recipe/home.html",variable)



@login_required(login_url="/login_page/")
def add_recipe(response):
    if response.method=="POST":
        name=response.POST.get("recipeName")
        photo=response.FILES.get("dishPhoto")
        op=response.POST.get("vegOrNonVeg")
        desc=response.POST.get("description")
        
        new_recipe=recipe(name=name,photo=photo,op=op,desc=desc)
        print("got it")
        new_recipe.save()
        print("Saved")
        return redirect("/add_recipe/")
    varibale={"usr":global_user}
    return render(response,"new_recipe/add_recipe.html",varibale)
    

def login_page(response):
    if response.method=="POST":
        username=response.POST.get("username")
        password=response.POST.get("password")
        user=authenticate(username=username,password=password)
        print(username,password,user)
        if user is not None:
            login(response,user)
            global global_user
            global_user = username
            return redirect("/add_recipe/")
        
            
    return render(response,"new_recipe/login_page.html")

def reg_page(response):
    if response.method=="POST":
        first=response.POST.get("first-name")
        last=response.POST.get("last-name")
        username=response.POST.get("username")
        email=response.POST.get("email")
        password=response.POST.get("password")
        if User.objects.filter(username=username).exists():
            return redirect("/reg_page/")
        user=User(first_name=first, last_name=last,email=email,username=username)
        user.save()
        u=User.objects.get(username=username)
        u.set_password(password)
        u.save()
        #login(response,user)
        return redirect("/login_page/")
    
    
    return render(response,"new_recipe/reg_page.html")

def logout_page(response):
    logout(response)     
    return redirect("/")