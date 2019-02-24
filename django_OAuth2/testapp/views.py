from rest_framework import viewsets


# Create your views here.

from .models import TestApp
from .serializers import TestAppSerializer

class TestAppViewSet(viewsets.ModelViewSet):

    queryset = TestApp.objects.all()
    serializer_class = TestAppSerializer