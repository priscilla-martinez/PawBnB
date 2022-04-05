from pkgutil import read_code
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .user import UserSerializer
from ..models.home import Home

class HomeSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Home
        fields = ('id', 'title', 'home_url', 'description', 'location', 'owner', 'created_at', 'updated_at', 'max_guests')
  