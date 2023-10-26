from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,UserSerializer as BaseUserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from djoser.serializers import TokenSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class SimpleUserCreateSerializer(BaseUserCreateSerializer):
    picture = serializers.ImageField(required=False)
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','email', 'password','first_name','last_name','picture']

class UserCreateSerializer(BaseUserCreateSerializer):
    picture = serializers.ImageField(required=False)
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','email', 'password','first_name','last_name','role','picture']

class UserSerializer(BaseUserSerializer):
    picture = serializers.ImageField(required=False)

    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'first_name', 'last_name','role','picture']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['role'] = user.role
        token['picture'] = str(user.picture.url) if user.picture else None
        token['email'] = user.email

        print(token['picture'])
        
        return token
    
