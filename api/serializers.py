from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price')

    def create(self, validated_data):
        product = Product.objects.create(
            title=validated_data.get('title'),
            price=validated_data.get('price')
        )
        return product
