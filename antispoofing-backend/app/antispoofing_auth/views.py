from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSignupSerializer
from .utils import create_user_account


class AuthView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        data = {"email": user.email, "username": user.username, "genre": user.genre}
        return Response(data=data, status=status.HTTP_201_CREATED)
