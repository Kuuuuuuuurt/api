from rest_framework import viewsets
from .serializers import MessageSerializer
from .models import Message

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()