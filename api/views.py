from rest_framework.views import APIView
from rest_framework.response import Response
from .helpers import execute_code
from .serializers import ExecuteCodeSerializer


class ExecuteCode(APIView):
    serializer_class = ExecuteCodeSerializer
    def post(self, request):
        serializer = ExecuteCodeSerializer(data=request.data)
        if(serializer.is_valid()):
            executed = execute_code(**serializer.data)
            return Response(executed)

