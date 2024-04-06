from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class FirstDevicesViewSet(viewsets.ModelViewSet):
    queryset = DevicesModel.objects.all()
    serializer_class = FirstDevicesSerializer

class SecondDevicesViewSet(viewsets.ModelViewSet):
    queryset = DevicesModel.objects.all()
    serializer_class = SecondDevicesSerializer
    
class OfficesViewSet(viewsets.ModelViewSet):
    queryset = OfficesModel.objects.all()
    serializer_class = OfficesSerializer

class DevicesModuleViewSet(viewsets.ModelViewSet):
    queryset = DevicesModuleModel.objects.all()
    serializer_class = DevicesModuleSerializer

class SectorViewSet(viewsets.ModelViewSet):
    queryset = SectorModel.objects.all()
    serializer_class = SectorSerializer
