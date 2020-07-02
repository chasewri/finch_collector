from .models import Finch
from rest_framework import viewsets, permissions
from .serializers import FinchSerializer

class FinchViewSet(viewsets.ModelViewSet):
    queryset = Finch.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FinchSerializer