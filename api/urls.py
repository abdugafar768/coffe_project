from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListView.as_view()),

    path('products/<int:category_pk>/',ProductListView.as_view()),

    path('baskets/', BasketListView.as_view()),
    
    path('orders/', OrderListView.as_view()),

    path('products/food/', FoodProductListView.as_view()),
    path('products/food/<int:pk>/', FoodProductDetailView.as_view()),
]
