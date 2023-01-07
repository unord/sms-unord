from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms
import pandas as pd


class MessageListView(generic.ListView):
    model = models.Message
    form_class = forms.MessageForm


class MessageCreateView(generic.CreateView):
    model = models.Message
    form_class = forms.MessageForm


class MessageDetailView(generic.DetailView):
    model = models.Message
    form_class = forms.MessageForm


class MessageUpdateView(generic.UpdateView):
    model = models.Message
    form_class = forms.MessageForm
    pk_url_kwarg = "pk"


class MessageDeleteView(generic.DeleteView):
    model = models.Message
    success_url = reverse_lazy("sms_app_Message_list")


class RecipientListView(generic.ListView):
    model = models.Recipient
    form_class = forms.RecipientForm


class RecipientCreateView(generic.CreateView):
    model = models.Recipient
    form_class = forms.RecipientForm


class RecipientDetailView(generic.DetailView):
    model = models.Recipient
    form_class = forms.RecipientForm


class RecipientUpdateView(generic.UpdateView):
    model = models.Recipient
    form_class = forms.RecipientForm
    pk_url_kwarg = "pk"


class RecipientDeleteView(generic.DeleteView):
    model = models.Recipient
    success_url = reverse_lazy("sms_app_Recipient_list")

class UploadSmsListView(generic.FormView):
    template_name = "sms_app/upload_sms_list.html"


def import_data(request):
    if request.method == 'POST':
        df_excel_file = pd.read_excel(request.FILES['formFile'])
        username = request.POST['username']
        inputGroupSelectMobile = request.POST['inputGroupSelectMobile']
        inputGroupSelectFistName = request.POST['inputGroupSelectFistName']
        inputGroupSelectLastName = request.POST['inputGroupSelectLastName']



    return render(request, 'sms_app/import.html', {'form': form})