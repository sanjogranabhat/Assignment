from django.shortcuts import render,redirect
from .models import Vegetables, Fruits

from.forms import AddVegetableForm,AddFruitForm,UpdateVegetableForm,UpdateFruitForm



# Create your views here.

def index(request):
    
    vegetable=Vegetables.objects.all()
    fruit =Fruits.objects.all()
    
    
    items ={
        'vegetables':vegetable,
        'fruits':fruit
    }
       
    return render(request,'Home/index.html',items)


# add vegetables

def add_vegetable(request):
    form = AddVegetableForm()
    if request.method == 'POST':
        form= AddVegetableForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin')  
    return render(request,'Home/add_vegetable.html',{'form':form})
    

# update vegetables

def update_vegetable(request,id):
    vegetable=Vegetables.objects.get(pk=id)
    form = UpdateVegetableForm(instance=vegetable)
    
    if request.method=='POST':    
        form = UpdateVegetableForm(request.POST,request.FILES, instance=vegetable)
        if form.is_valid():
            form.save()
            return redirect('admin')
    return render(request,'Home/update_vegetable.html',{'form':form})


# delete vegetables

def delete_vegetable(request,id):
    vegetable=Vegetables.objects.get(pk=id)
    vegetable.delete()
    return redirect('admin')


# add fruits

def add_fruit(request):
    form = AddFruitForm()
    if request.method =='POST':
        form = AddFruitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin')
    return render(request,'Home/add_fruit.html',{'form':form})

# Update Fruits 

def update_fruit(request,id):
    fruit=Fruits.objects.get(pk=id)
    form = UpdateFruitForm(instance=fruit)
    
    if request.method=='POST':    
        form = UpdateFruitForm(request.POST,request.FILES, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('admin')
    return render(request,'Home/update_fruit.html',{'form':form})

# delete fruit

def delete_fruit(request,id):
    fruit=Fruits.objects.get(pk=id)
    fruit.delete()
    return redirect('admin')



# admin page

def admin(request):
    
    vegetable=Vegetables.objects.all()
    fruit =Fruits.objects.all()
    
    
    items ={
        'vegetables':vegetable,
        'fruits':fruit
    }
       
    return render(request,'Home/admin.html',items)


      
        
    