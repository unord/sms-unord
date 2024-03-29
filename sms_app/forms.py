from django import forms
from sms_app.models import Message
from django.contrib.auth.models import User
from . import models
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django.utils.translation import gettext_lazy as _

DATETIME_FORMAT = '%d/%m/%Y %H:%M'

class RecipientForm(forms.ModelForm):
    mobile_number = forms.CharField(label=_("Mobilnummer"), required=True, max_length=8, widget=forms.TextInput(
        attrs={'class': 'form-control',  'type': 'number'}))
    first_name = forms.CharField(label=_("Fornavn"), max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    last_name = forms.CharField(label=_("Efternavn"), max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control',  }))

    class Meta:
        model = models.Recipient
        fields = [
            "mobile_number",
            "first_name",
            "last_name",
        ]





class MessageForm(forms.ModelForm):
    email = forms.EmailField(label=_("Email"), required=True, max_length=30, widget=forms.EmailInput(
        attrs={'class': 'form-control', }))
    message = forms.CharField(label=_("Sms besked"), required=True, max_length=600, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5, }))
    time_to_send = forms.DateTimeField(input_formats=[DATETIME_FORMAT],
                                             widget=DateTimePickerInput(format=DATETIME_FORMAT),
                                             label=_("Hvornår skal smserne sendes"), required=True, )

    class Meta:
        model = models.Message
        fields = [
            "email",
            "message",
            "time_to_send",
        ]



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