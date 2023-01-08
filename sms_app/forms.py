from django import forms
from django.contrib.auth.models import User
from sms_app.models import Message
from . import models


class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = [
            "link_code",
            "time_to_send",
            "completed",
            "message",
            "user",
        ]

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields["user"].queryset = User.objects.all()



class RecipientForm(forms.ModelForm):
    class Meta:
        model = models.Recipient
        fields = [
            "mobile_number",
            "first_name",
            "sent",
            "last_name",
            "message",
        ]

    def __init__(self, *args, **kwargs):
        super(RecipientForm, self).__init__(*args, **kwargs)
        self.fields["message"].queryset = Message.objects.all()

class UploadEXcelForm(forms.ModelForm):
    class Meta:
        fields = [
            "user",
            "time_to_send",
            "message",
            "excel_file",
        ]

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields["user"].queryset = User.objects.all()