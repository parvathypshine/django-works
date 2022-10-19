from rest_framework import serializers
from api.models import Reviews,Bikes,Cart
from django.contrib.auth.models import User
class BikeSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    qty=serializers.IntegerField()
    fuel=serializers.CharField()

    def create(self, validated_data):
        return Bikes.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get("name")
        instance.price = validated_data.get("price")
        instance.qty = validated_data.get("qty")
        instance.fuel=validated_data.get("fuel")
        instance.save()
        return instance

    def validate(self, data):
        qty = data.get("qty")
        price = data.get("price")

        if qty not in range(50, 1000):
            raise serializers.ValidationError("invalid qty")
        if price not in range(50, 1000):
            raise serializers.ValidationError("invalid price")
        return data
        # price=data.get("price")


class ReviewSerializer(serializers.ModelSerializer):
    created_date=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"
            # ["book","user","comment","rating"]
        # exclude=("created_date",)

        # def validate(self,data):
        #     qty=data.get("qty")
        #     if qty not in range(50,1000):
        #         raise serializers.ValidationError("invalid qty")
        #     if price not in range(50,1000):
        #         raise serializers.ValidationError("invalid price")
        #     return data
        #     # price=data.get("price")
#  viewset and modelview set put and post is not working.... 21 and 22 date vheck

#check put method of viewset
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name',"username",'email','password']

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class CartSerializer(serializers.ModelSerializer):
        bike=serializers.CharField(read_only=True)
        user=serializers.CharField(read_only=True)
        status=serializers.CharField(read_only=True)
        class Meta:
            model=Cart
            fields=['bike','user','status']