from .models import students
from .serializer import RegisterSerializer, LoginSerializer, StudentsSerializer

from rest_framework.views import APIView
from rest_framework import status, generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout, login

class StudentsViewset(viewsets.ModelViewSet):
    queryset = students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated]
    
class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    
class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self,  request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer._validated_data['user']
        
        login(request, user)
        token, created = Token.objects.get_or_create(user = user)
        return Response({
            'token': token.key,
            'username': user.username,
            'email': user.email
        })
        
class logoutView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"Logout Successfully"}, status=status.HTTP_200_OK)