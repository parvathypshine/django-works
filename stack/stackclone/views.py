from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
# Create your views here.
class RegisterView(ViewSet):
    def get(self,request,*args,**kwargs):


