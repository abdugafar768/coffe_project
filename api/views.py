from .serializers import *
from .models import *
from rest_framework import permissions , generics
from rest_framework.response import Response
from rest_framework import status


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FoodProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = FoodProductSerializer

class DrinkProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = DrinkProductSerializer

class FoodProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = FoodProductDetailSerializer

class BasketListView(generics.ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
       
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
