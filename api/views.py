from rest_framework.views import APIView
from rest_framework.response import Response
from .helpers import execute_code
from django.contrib.auth.models import User
from .serializers import (
    ExecuteCodeSerializer,
    PostSerializerCreate,
    UserRegistrationSerializer,
    PostSerializer
)

from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import viewsets
from .models import Post

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


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]


    def get_serializer_class(self):
        if(self.request.method == "POST"):
            return PostSerializerCreate
        return self.serializer_class
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        if(self.request.method == "POST"):
            context["user"] = self.request.user.id
        return context
    
    def create(self, request, *args, **kwargs):
        print(request.user)
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)