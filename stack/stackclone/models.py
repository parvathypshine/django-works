from django.db import models

# Create your models here.
class Clone(models.Model):
    user=models.CharField(max_length=150)
