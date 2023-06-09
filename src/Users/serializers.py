from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'email': {
                'style': {'input_type': 'email'}
            },
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }