from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Bikes(models.Model):
    name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    qty=models.PositiveIntegerField(default=1)
    fuel=models.CharField(max_length=100)
    # is_active=models.BooleanField(default=)

    def __str__(self):
        return self.name
#
class Reviews(models.Model):
    bike=models.ForeignKey(Bikes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=150)
    rating=models.PositiveIntegerField()
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Cart(models.Model):
    bike=models.ForeignKey(Bikes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=("in-cart","in-cart"),
    ("cancelled","cancelled"),
    ("order-placed","order-placed")
    status=models.CharField(max_length=120,choices=options,default='in-cart')