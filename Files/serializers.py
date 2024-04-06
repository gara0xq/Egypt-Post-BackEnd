from rest_framework import serializers
from .models import *


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = ['title', 'description', 'file', 'sender', 'receiver']
    
    def create(self, data):
        title = data.pop('title', None)
        description = data.pop('description', None)
        file = data.pop('file', None)
        sender = data.pop('sender', None)
        receiver = data.pop('receiver', None)

        data['title'] = title
        data['description'] = description
        data['file'] = file
        data['sender'] = sender
        data['receiver'] = receiver

        return MessageModel.objects.create(**data)