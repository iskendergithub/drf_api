from django.shortcuts import render
from .models import Product
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CreateProductSerializer


class ProductCreateView(APIView):
    """Creating APIView for product"""

    def post(self, request):
        product = CreateProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
        return Response(status=201)

