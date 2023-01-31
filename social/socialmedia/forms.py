from socket import fromshare

from django import forms
from socialmedia.models import MyUser,Posts
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    class Meta:
        model=MyUser
        fields=["first_name","last_name","username","email","phone", 
        "profile_pic","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["image",]
        widgets={
                 "image":forms.FileInput(attrs={"class":"form-select"})
        }

# class PostForm(forms.Form):
#     answer=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))