from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    phone=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to="profilepics",null=True)



class Posts(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    created_date=models.DateField(auto_now_add=True)
    
class Comment(models.Model):
    posts=models.ForeignKey(Posts,on_delete=models.CASCADE)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    created_date=models.DateField(auto_now_add=True)