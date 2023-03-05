from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    size = serializers.CharField(max_length=30)
    producer_id = serializers.IntegerField()
    cat_id = serializers.IntegerField()
    cost = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    def update(self, instance, validated_data,pk):
        instance.title = validated_data.get('title', instance.title),
        instance.size = validated_data.get('size', instance.size),
        instance.producer_id = validated_data.get('producer_id', instance.producer_id),
        instance.cat_id = validated_data.get('cat_id', instance.cat_id),
        instance.cost = validated_data.get('cost', instance.cost),
        instance.save()
        return instance


class ProducerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=30)

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)