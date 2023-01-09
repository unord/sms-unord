from django.contrib import admin
from django import forms

from . import models


class MessageAdminForm(forms.ModelForm):

    class Meta:
        model = models.Message
        fields = "__all__"


class MessageAdmin(admin.ModelAdmin):
    form = MessageAdminForm
    list_display = [
        "last_updated",
        "completed",
        "message",
        "email",
        "link_code",
        "time_to_send",
        "created",
        "validated_by_email",
    ]
    readonly_fields = [
        "last_updated",
        "completed",
        "message",
        "email",
        "link_code",
        "time_to_send",
        "created",
        "validated_by_email",
    ]
