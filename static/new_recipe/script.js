console.log("I am In")
non_veg_recipe=document.getElementsByClassName("food-type")
function filter(checkbox)
{
    
    if (checkbox.checked)
    {
      l=non_veg_recipe.length
      for(let i=0;i<l;i++)
      {
        if (non_veg_recipe[i].innerHTML=="nonveg")
        {
            non_veg_recipe[i].closest(".food-container").style.display="none";
        }
      }
      console.log("veg only activated")
    }
    else{

        for(let i=0;i<l;i++)
      {
        if (non_veg_recipe[i].innerHTML=="nonveg")
        {
            non_veg_recipe[i].closest(".food-container").style.display="flex";
        }
      }

        console.log("no filter is activated")

    }
}