from django.shortcuts import render,redirect
from new_recipe.models import recipe
from new_recipe.models import vegModel

# Create your views here.
def home(response):
    check=False
    r1=recipe.objects.all()
    if response.method=="GET":
        isveg=response.GET.get("veg")
        if isveg:
            check=True
            r2=vegModel.objects.all()[0]
            r2.isVeg=True
            r1=recipe.objects.filter(op="veg")
        else:
              r1=recipe.objects.all()
              r2=vegModel.objects.all()[0]
              r2.isVeg=False
              check=False
                
    variable={"recipes":r1,"check":check}
    
    return render(response,"new_recipe/home.html",variable)




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
    return render(response,"new_recipe/add_recipe.html")