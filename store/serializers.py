from rest_framework import serializers
from .models import Product, Category
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'date_joined', 'last_login')

class ProductSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
    
    
    def to_representation(self, instance):
        rep = super(ProductSerializer, self).to_representation(instance)
        rep['category'] = instance.category.name
        return rep

class ProductListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ('author', 'description', 'category', 'phone_number')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'