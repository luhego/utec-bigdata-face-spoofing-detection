from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSignupSerializer, UserLoginSerializer
from .utils import create_user_account, register_login_attempt


class SignupView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        data = {"email": user.email, "username": user.username}
        return Response(data=data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = register_login_attempt(**serializer.validated_data)
        data = {"email": user.email, "username": user.username}
        return Response(data=data, status=status.HTTP_200_OK)
