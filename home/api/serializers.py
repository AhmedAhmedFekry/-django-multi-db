from rest_framework import serializers
from home.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Product
        fields = '__all__'
    def create(self, validated_data):
        obj = Product.objects.using("users_db").create(**validated_data)
        obj.save()
        return obj