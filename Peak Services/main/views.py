from operator import truediv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login 
from .models import InventoryItem, ScheduleItem, Transaction
from django.contrib.auth.forms import UserCreationForm 
from datetime import date




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

def inventory(request):
    search = request.GET.get('search', '')

    items = InventoryItem.objects.all()

    if search:
        items = items.filter(name__icontains=search)

    return render(request, 'main/inventory.html', {
        'items': items,
        'search': search
    })


def add_item(request):
    if request.method == 'POST':

        name = request.POST['name']
        category = request.POST['category']
        quantity = request.POST['quantity']
        product_link = request.POST.get('product_link')


        InventoryItem.objects.create(
            name=name,
            category=category,
            quantity=quantity,
            product_link=product_link

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


# Schedule module

def schedule(request):
    today = date.today()
    items = ScheduleItem.objects.all().order_by('date', 'time')
    upcoming_items = ScheduleItem.objects.filter(date__gte=today).order_by('date', 'time')[:5]

    return render(request, 'main/schedule.html', {'items': items, 'today': today, 'upcoming_items': upcoming_items,})

def add_schedule(request):
    if request.method == 'POST':
        ScheduleItem.objects.create(title=request.POST['title'],
        description=request.POST['description'],
        date=request.POST['date'],
        time=request.POST['time'],

        item_type=request.POST['item_type'])



        return redirect('schedule')

def complete_schedule(request, item_id):
    item = get_object_or_404(ScheduleItem, id=item_id)
    
    if request.method == 'POST':
        item.completed = True 
        item.save()

        return redirect('schedule')

def delete_schedule(request, item_id):

    item = get_object_or_404(ScheduleItem, id=item_id)

    if request.method == 'POST':
        item.delete()

        return redirect('schedule')


# finance module

def finance(request):
    transactions = Transaction.objects.all().order_by('-date')

    income = 0
    expenses = 0

    for transaction in transactions:
        if transaction.transaction_type == 'Income':
            income += transaction.amount
        else:
            expenses += transaction.amount

  
    profit = income - expenses

    return render(request, 'main/finance.html', {
        'transactions': transactions,
        'income': income,
        'expenses': expenses,
        'profit': profit,
    })


def add_transaction(request):
    if request.method == 'POST':
        Transaction.objects.create(
            description=request.POST['description'],
            amount=request.POST['amount'],
            transaction_type=request.POST['transaction_type'],
            category=request.POST['category'],
            date=request.POST['date'],
        )

    return redirect('finance')


def delete_transaction(request, item_id):
    transaction = get_object_or_404(Transaction, id=item_id)

    if request.method == 'POST':
        transaction.delete()

    return redirect('finance')