from rest_framework import serializers

class ExecuteCodeSerializer(serializers.Serializer):
    runtime = serializers.CharField(max_length=100)
    version = serializers.CharField(max_length=10)
    code = serializers.CharField()