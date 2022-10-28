from django.urls import path
from .views import (
    ProductCreateAPIView,
    ProductDetailView,
    UpdateProductView,
    )

urlpatterns = [
    path('product-create/', ProductCreateAPIView.as_view()),
    path('product-detail/<int:pk>/', ProductDetailView.as_view()),
    path('product-update/<int:pk>/', UpdateProductView.as_view()),
]
