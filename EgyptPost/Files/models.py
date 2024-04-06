from django.db import models

class MessageModel(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(blank = True)
    file = models.FileField(upload_to='files/')
    sender = models.CharField(max_length = 255)
    receiver = models.CharField(max_length = 255)