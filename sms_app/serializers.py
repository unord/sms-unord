from rest_framework import serializers

from . import models


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Message
        fields = [
            "link_code",
            "time_to_send",
            "last_updated",
            "completed",
            "message",
            "created",
            "user",
        ]

class RecipientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Recipient
        fields = [
            "mobile_number",
            "last_updated",
            "first_name",
            "created",
            "sent",
            "last_name",
            "message",
        ]
