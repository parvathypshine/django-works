from django.db import models
from django.db import models
# Create your models here.
class Dishes(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    rating=models.PositiveIntegerField()