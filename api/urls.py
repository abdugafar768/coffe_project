from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/food/', FoodProductListView.as_view(), name='food-product-list'),
    path('products/drink/', DrinkProductListView.as_view(), name='drink-product-list'),
    path('products/food/<int:pk>/', FoodProductDetailView.as_view(), name='food-product-detail'),
    path('baskets/', BasketListView.as_view(), name='basket-list'),
    path('orders/', OrderListView.as_view(), name='order-list'),
]