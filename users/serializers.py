from rest_framework import serializers
from django.contrib.auth import get_user_model
from store.serializers import ProductListSerializer

UserModel = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password", )

class UserSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True)
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'date_joined', 'last_login', 'products')
        depth = 1