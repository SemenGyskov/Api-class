from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    size = serializers.CharField(max_length=30)
    producer_id = serializers.IntegerField()
    cat_id = serializers.IntegerField()
    cost = serializers.IntegerField()

class ProducerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=30)

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)