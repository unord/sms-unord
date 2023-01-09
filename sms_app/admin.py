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
        "user.username",
        "email",
        "time_to_send",
        "message",
        "link_code",
        "validated_by_email",
        "completed",
        "last_updated",
        "created",
    ]
    readonly_fields = [

    ]


class RecipientAdminForm(forms.ModelForm):

    class Meta:
        model = models.Recipient
        fields = "__all__"


class RecipientAdmin(admin.ModelAdmin):
    form = RecipientAdminForm
    list_display = [
        "mobile_number",
        "first_name",
        "last_name",
        "message",
        "sent",
        "last_updated",
        "created",
    ]
    readonly_fields = [

    ]


admin.site.register(models.Message, MessageAdmin)
admin.site.register(models.Recipient, RecipientAdmin)