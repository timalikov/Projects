from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import Category, Furniture, Order, User
from api.serializers import UserSerializer, CategorySerializer, FurnitureSerializer, CustomTokenObtainPairSerializer, \
    CustomTokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import LimitOffsetPagination

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        return Category.objects.filter(id=id)


class CategoryFurnitureList(generics.ListAPIView):
    serializer_class = FurnitureSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('id')
        return Furniture.objects.filter(category_id=category_id)


class FurnitureListView(generics.ListCreateAPIView):
    serializer_class = FurnitureSerializer
    permission_classes = (AllowAny,)
    queryset = Furniture.objects.all()


class FurnitureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    lookup_field = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        return Furniture.objects.filter(id=id)


@api_view(['POST'])
def create_order(request):
    furniture_id = request.data.get('furniture_id')
    address = request.data.get('address')
    phone_number = request.data.get('phone_number')
    user = request.user

    furniture = get_object_or_404(Furniture, id=furniture_id)

    order = Order.objects.create(furniture=furniture, user=user, address=address, phoneNumber=phone_number)

    serializer = OrderSerializer(order)
    return Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=make_password(validated_data['password']),
        )
        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username'

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = request.user
    # Return user information or null
    if user.is_authenticated:
        return Response({
            'username': user.username,
            'email': user.email
        })
    else:
        return Response(None)