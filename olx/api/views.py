from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import BikeSerializer,ReviewSerializer,UserSerializer,CartSerializer
from api.models import Bikes,Reviews,Cart
from rest_framework.viewsets import ViewSet,ModelViewSet

from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from rest_framework.decorators import action

class ProductsView(APIView):
    # def post(self, request, *args, **kwargs):
    #     bname=request.data.get('name')
    #     bauthor = request.data.get('author')
    #     bprice= request.data.get('price')
    #     bpublisher= request.data.get('publisher')
    #     Books.objects.create(name=bname,author=bauthor,price=bprice,publisher=bpublisher)
    #     return Response(data="created")

    def get(self, request, *args, **kwargs):
        qs=Bikes.objects.all()
        serializer=BikeSerializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer=BikeSerializer(data=request.data)
        if serializer.is_valid():
            Bikes.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        #     print(serializer.validated_data)
        # else:
        #     return Response(data=serializer.errors)
        # return Response(data="created")


    # Books.objects.data(**serializer.validated_data)
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)

class ProductDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("id")
        bike=Bikes.objects.get(id=id)
        serializer=BikeSerializer(bike,many=False)
        return Response(data=serializer.data)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        Bikes.objects.get(id=id).delete()
        return Response(data="deleted")

    def put(self, request, *args, **kwargs):
        id=kwargs.get('id')
        serializer=BikeSerializer(data=request.data)
        if serializer.is_valid():
            Bikes.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ReviewView(APIView):
    def get(self, request, *args, **kwargs):
        reviews=Reviews.objects.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ReviewDetailsView(APIView):
    def get(self,request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(qs,many=False)
        return Response(data=serializer.data)

    def put(self,request, *args, **kwargs):
        id=kwargs.get("pk")
        object=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(instance=object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request, *args, **kwargs):
        id=kwargs.get("pk")
        Reviews.objects.get(id=id).delete()
        return Response(data="deleted")

class ProductsViewsetView(ViewSet):
    # authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]



    def list(self,request,*args,**kwargs):
        qs=Bikes.objects.all()
        serializer=BikeSerializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=BikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        bike=Bikes.objects.get(id=id)
        serializer=BikeSerializer(bike,many=False)
        return Response(data=serializer.data)
    def update(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        bike=Bikes.objects.get(id=id)
        serializer=BikeSerializer(instance=bike,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Bikes.objects.get(id=id).delete()
        return Response(data="deleted")
    @action(methods=['POST'],detail=True)
    def add_review(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        bike=Bikes.objects.get(id=id)
        user=request.user
        Reviews.objects.create(bike=bike,user=user,comment=request.data.get('comment'),rating=request.data.get('rating'))
        return Response(data="created")

    @action(methods=['GET'],detail=True)
    def get_review(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        bike=Bikes.objects.get(id=id)
        reviews=bike.reviews_set.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)

    @action(methods=["POST"],detail=True)
    def addto_cart(self,request,*args,**kwargs):
        id = kwargs.get('pk')
        bike = Bikes.objects.get(id=id)
        Cart.objects.create(bike=bike,user=request.user)
        return Response(data="created")

    # @action(methods=['GET'],detail=True)
    # def cart_list(self,request,*args,**kwargs):
    #     cart=Cart.objects.all()
    #     cart_list=cart.bikes_set.all()
    #     serializer=CartSerializer(cart_list,many=True)
    #     return Response(data=serializer.data)


    # @action(methods=['POST'],detail=True)
    # def add_cart(self,request,*args,**kwargs):
    #     id=kwargs.get('pk')
    #     bike=Bikes.objects.get(id=id)
    #     return Response(data='added to cart')
    #

class ProductModelviewsetview(ModelViewSet):
    serializer_class = BikeSerializer

    queryset=Bikes.objects.all()

class ReviewModelViewsetView(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Reviews.objects.all()

    def list(self, request, *args, **kwargs):
        all_reviews=Reviews.objects.all()

        if "user" in request:
            all_reviews=all_reviews.filter(user=request.query_params.get('user'))
            serializer = ReviewSerializer(all_reviews, many=True)
            return Response(data=serializer.data)
# check reviewmodelview#

class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
