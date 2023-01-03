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
        "link_code",
        "time_to_send",
        "last_updated",
        "completed",
        "message",
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
        "last_updated",
        "first_name",
        "created",
        "sent",
        "last_name",
    ]
    readonly_fields = [

    ]


admin.site.register(models.Message, MessageAdmin)
admin.site.register(models.Recipient, RecipientAdmin)