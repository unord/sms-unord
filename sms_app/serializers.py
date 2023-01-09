from rest_framework import serializers

from . import models


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Message
        fields = [
            "last_updated",
            "completed",
            "message",
            "email",
            "link_code",
            "time_to_send",
            "created",
            "validated_by_email",
            "user",
        ]

class RecipientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Recipient
        fields = [
            "created",
            "last_name",
            "mobile_number",
            "sent",
            "last_updated",
            "first_name",
            "message",
        ]