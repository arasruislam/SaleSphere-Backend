from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AdminModel


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


# Admin serializer
class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = AdminModel
        fields = ["id", "is_admin", "profile_img", "user"]
