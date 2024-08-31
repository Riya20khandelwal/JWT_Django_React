from django.shortcuts import render

from api.models import Profile, User
from api.serializer import UserSerializer, MyTokenObtainPairSerializer

from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    pass
