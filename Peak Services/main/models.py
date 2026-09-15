
from pickle import TRUE
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

    def __str__(self):
        return self.title

