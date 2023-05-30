from django.urls import path
from .views import ProtectedView, ProductListAPIView, ProductDetailAPIView


urlpatterns = [
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('products-list/', ProductListAPIView.as_view(), name='product-list'),
    path('products-details/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail')

]