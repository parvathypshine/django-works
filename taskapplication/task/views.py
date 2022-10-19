from django.shortcuts import render,redirect
from task.forms import LoginForm, RegistrationForm
from task.models import Task
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
from django.views.generic import View
class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class LogView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")

class Registerview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"register.html")

        # add task View 
class AddTaskView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"addtask.html")

    def post(self,request,*args,**kwargs):
        name=request.user
        task=request.POST.get("task")
        Task.objects.create(task_name=task,user=name)
        return redirect('todo-all')

      
      
class TaskListView(View):
    def get(self,request,*args,**kwargs):
        # qs=Task.objects.filter(user=request.user)
        qs=request.user.task_set.all()
        return render(request,"tasklist.html",{"todos":qs})


    #{{}} - simple task
    # complex {%}
class TaskDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        task=Task.objects.get(id=id)
        return render(request,'task-detail.html',{"todo":task})


class TaskDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Task.objects.filter(id=id).delete()
        return redirect("todo-all")

class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,'register.html',{"form":form})

    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("todo-all")
        else:
            return render(request,'register.html',{'form':form})


class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'login.html',{"form":form})

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("todo-all")
            else:
               return render(request,"login.html",{"form":form})


def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")