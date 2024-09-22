from .serializers import AdminSerializer, StaffSerializer
from django.contrib.auth.tokens import default_token_generator
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AdminModel, Staff
from rest_framework import viewsets
from rest_framework import status


# Create your views here.
class AdminApiView(viewsets.ReadOnlyModelViewSet):
    queryset = AdminModel.objects.all()
    serializer_class = AdminSerializer


# staff model view set
class StaffApiView(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
