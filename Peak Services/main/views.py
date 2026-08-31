from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login 
from .models import InventoryItem
from django.contrib.auth.forms import UserCreationForm 



def home(request):
    return render(request, 'main/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = UserCreationForm()

    return render (request, 'main/signup.html', {'form': form})

# INVENTORY

def home(request):
    return render(request, 'main/index.html')

def inventory(request):
    return render(request, 'main/inventory.html')

def inventory(request):
    items = InventoryItem.objects.all()

    return render(request, 'main/inventory.html', {
        'items': items
    })


def add_item(request):
    if request.method == 'POST':

        name = request.POST['name']
        category = request.POST['category']
        quantity = request.POST['quantity']

        InventoryItem.objects.create(
            name=name,
            category=category,
            quantity=quantity
        )

    return redirect('inventory')


def delete_item(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id)
    item.delete()

    return redirect('inventory')


def update_stock(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id)

    if request.method == 'POST':
        item.quantity = request.POST['quantity']
        item.save()

    return redirect('inventory')