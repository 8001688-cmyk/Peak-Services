
from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    product_link = models.URLField(blank=True)

    def __str__(self):
        return self.name

# Schedule stuff

class ScheduleItem(models.Model):
    TYPE_CHOICES = [
        ('Meeting', 'Meeting'),
        ('Deal', 'Deal'),
        ('Task', 'Task'),
        ('Other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=TRUE)
    date = models.DateField()
    time = models.TimeField()
    item_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Task')

    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# finance module

class Transaction(models.Model):
    
    TYPES = [
        ('Income', 'Income'),
        ('Expense', 'Expense')
        
        ]
    
    CATEGORIES = [
        ('Sales', 'Sales'),
        ('Services', 'Services'),
        ('Inventory', 'Inventory'),
        ('Rent', 'Rent'),
        ('Utilities', 'Utilities'),
        ('Wages', 'Wages'),
        ('Marketing', 'Marketing'),
        ('Other', 'Other'),

        
        
        ]

    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TYPES)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    date = models.DateField()

    def __str__(self):
        return self.description

