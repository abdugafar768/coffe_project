from .serializers import *
from .models import *
from rest_framework import permissions , generics
from rest_framework.response import Response
from rest_framework import status
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = DrinkProductSerializer

    def get_queryset(self):
        category_pk = self.kwargs['category_pk']
        return Product.objects.filter(category_id=category_pk)
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     filtered_data = PatientFilter(self.request.GET, queryset=queryset)
    #     return filtered_data.qs

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = DrinkProductSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, )
    filterset_class = ProductFilter

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = DrinkProductSerializer

class FoodProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = FoodProductDetailSerializer


class FoodProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = FoodProductDetailSerializer


class BasketListView(generics.ListCreateAPIView):
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
    

class OrderListView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
