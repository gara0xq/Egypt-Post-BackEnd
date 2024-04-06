from rest_framework import viewsets
from .models import *
from .serializers import *

class MessageViewSet(viewsets.ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer