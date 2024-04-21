from django import forms
from.models import Vegetables,Fruits

#add vegetables

class AddVegetableForm(forms.ModelForm):
    class Meta:
        model = Vegetables
        fields =['image','name','price','quantity','description']
        

# Update vegetable form
class UpdateVegetableForm(forms.ModelForm):
    class Meta:
        model = Vegetables
        fields =['image','name','price','quantity','description']
        
        
#add fruits 
class AddFruitForm(forms.ModelForm):
    class Meta:
        model = Fruits
        fields =['image','name','quantity','price','description']    


# Update fruits form

class UpdateFruitForm(forms.ModelForm):
    class Meta:
        model = Fruits
        fields =['image','name','quantity','price','description']