from rest_framework import viewsets, permissions

from . import serializers
from . import models


class MessageViewSet(viewsets.ModelViewSet):
    """ViewSet for the Message class"""

    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecipientViewSet(viewsets.ModelViewSet):
    """ViewSet for the Recipient class"""

    queryset = models.Recipient.objects.all()
    serializer_class = serializers.RecipientSerializer
    permission_classes = [permissions.IsAuthenticated]