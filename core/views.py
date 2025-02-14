from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

User = get_user_model()

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

class UserProfileView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "phone_number": user.phone_number,
                "address": user.address
            }, status=status.HTTP_200_OK)
        return Response({"error": "Not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
    

class HelthCheck(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"massage":'ok !'})
