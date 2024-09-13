from .serializers import AdminSerializer
from .models import AdminModel
from rest_framework import viewsets

# Create your views here.
class AdminApiView(viewsets.ReadOnlyModelViewSet):
    queryset = AdminModel.objects.all()
    serializer_class = AdminSerializer
