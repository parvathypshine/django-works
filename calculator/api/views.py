from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class AddView(APIView):
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        sum=n1+n2
        return Response({'result':sum})

class SubView(APIView):
    def post(self,request,*args,**kwargs):
        n1=int(request.data.get("num1"))
        n2=int(request.data.get("num2"))
        sub=n1-n2
        return Response({'result':sub})
        
class FactView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return Response({'result':fact})
        


