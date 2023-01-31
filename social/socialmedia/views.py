from django.shortcuts import render,redirect
from socialmedia.models import  MyUser,Posts
from socialmedia.forms import RegistrationForm,LoginForm,PostForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView,DetailView,ListView,TemplateView,FormView
# Create your views here.

# class SignupView(CreateView):
#     model=MyUser
#     form_class=RegistrationForm
#     template_name="register.html"
#     success_url=reverse_lazy("register")

class SignupView(CreateView):
    model=MyUser
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("register")

class Loginview(FormView):
    form_class=LoginForm
    template_name="login.html"
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render(request,self.template_name,{"form":form})

class IndexView(CreateView,ListView):
    template_name="home.html"
    form_class=PostForm
    model=Posts
    success_url=reverse_lazy("index")
    context_object_name="post"

class PostDetailsView(DetailView,FormView):
    model=Posts
    template_name="post-detail.html"
    pk_url_kwarg: str="id"
    context_object_name: str="post"
    form_class=PostForm
