from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class ExecuteCodeSerializer(serializers.Serializer):
    runtime = serializers.CharField(max_length=100)
    version = serializers.CharField(max_length=10)
    code = serializers.CharField()


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('password')
        return ret


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username"]


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Post
        fields = ['id', 'title', 'user', 'image']


class PostSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'image']
