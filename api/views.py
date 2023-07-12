from rest_framework.views import APIView
from rest_framework.response import Response
from .helpers import execute_code
from django.contrib.auth.models import User
from .serializers import (
    ExecuteCodeSerializer,
    UserRegistrationSerializer
)



class ExecuteCode(APIView):
    serializer_class = ExecuteCodeSerializer

    def post(self, request):
        serializer = ExecuteCodeSerializer(data=request.data)
        if (serializer.is_valid()):
            executed = execute_code(**serializer.data)
            return Response(executed)


class RegisterUser(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if(serializer.is_valid()):
            user = User(**serializer.data)
            user.save()
            return Response(serializer.data)
