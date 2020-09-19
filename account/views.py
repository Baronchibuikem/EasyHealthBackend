from django.contrib.auth.models import User
from rest_framework import status, generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from account.models import CustomUser
from knox.models import AuthToken
from rest_framework.permissions import AllowAny
from account.permissions import IsOwnerOrReadonly
from account.serializers import (RegistrationSerializer, LoginSerializer, GetUserSerializer)
from collections import OrderedDict
from django.db.models import F, Count


class LoginViewSet(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            return Response({
                "user": GetUserSerializer(user, context=self.get_serializer_context()).data,
                # 'user': user.pk,
                "token": AuthToken.objects.create(user)[1],
                "status": status.HTTP_200_OK,
                "message": "Login successfully"
            })
        else:
            return Response({
                "error": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            })


class RegisterViewSet(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({
                "user": user.pk,
                "token": AuthToken.objects.create(user)[1],
                "status": status.HTTP_201_CREATED,
                "message": "Account created successfully"
            })


class UserListAPIView(generics.ListAPIView):
    """
    This endpoint is used for listing all registered users in the platform,
    but only an admin user can access the data in this endpoint
    """
    queryset = CustomUser.objects.all()
    serializer_class = GetUserSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    """
    For retrieving a single user from the database.
    """
    queryset = CustomUser.objects.all()
    serializer_class = GetUserSerializer
    permission_classes = (IsOwnerOrReadonly, )

    def get(self, request, pk, format=None):
        try:
            user_info = OrderedDict()
            user = self.get_object()
            serializer = GetUserSerializer(
            user, context=self.get_serializer_context())
            user_info['user'] = serializer.data
            print(user_info)
            return Response({"user_details": user_info, "status":status.HTTP_200_OK})
        except:
            return Response({"status": "User ID not found"})

