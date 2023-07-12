from rest_framework import serializers

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