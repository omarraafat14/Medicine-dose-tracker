from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
