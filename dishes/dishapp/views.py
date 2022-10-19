from django.shortcuts import render
from dishapp.models import Dishes
from django.views.generic import View
# Create your views here.
class AddView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add.html")

    def post(self,request,*args,**kwargs):
        name=request.POST.get()