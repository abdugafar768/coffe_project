from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'description', 'created_at', 'updated_at']


SIZE_CHOICES = (
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
    ('Extra Large', 'Extra Large'),
    )

SWEETENER_CHOICES = (
    ('Sugar', 'Sugar'),
    ('Splenda', 'Splenda'),
    ('Stevia', 'Stevia'),
)



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class DrinkProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'




class DrinkProductDetailSerializer(serializers.ModelSerializer):
    size = serializers.ChoiceField(choices=SIZE_CHOICES)
    sweeteners = serializers.ChoiceField(choices=SWEETENER_CHOICES)
    quantity = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ['id','image','title','size','sweeteners','quantity']

class FoodProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


        
# class FoodProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
