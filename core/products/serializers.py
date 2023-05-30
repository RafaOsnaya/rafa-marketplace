from rest_framework import serializers
from .models import Product
# Category

# class CategorySerializer(serializers.ModelSerializer):
    
#     category_name = serializers.CharField(required=False)
    
#     class Meta:
#         model = Category
#         fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # imagen = serializers.ImageField(required=False)
    # categoria = CategorySerializer(many=True,)

    class Meta:
        model = Product
        fields = '__all__'

