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

class UploadSmsListView(generic.TemplateView):
    template_name = "sms_app/upload_sms_list.html"


def import_data(request):
    print("pre-post")
    if request.method == 'POST':
        print("post")
        df_excel_file = pd.read_excel(request.FILES['filename'])
        print(df_excel_file)
        username = request.POST['username']
        inputGroupSelectMobile = request.POST['inputGroupSelectMobile']
        inputGroupSelectFistName = request.POST['inputGroupSelectFistName']
        inputGroupSelectLastName = request.POST['inputGroupSelectLastName']

        mobile_error = []
        row_count = 0

        for index, row in df_excel_file.iterrows():
            row_count += 1
            mobile = row[inputGroupSelectMobile]
            mobile = str(mobile)
            mobile = mobile.replace(" ", "")
            mobile = mobile.replace("-", "")
            mobile = mobile.replace("(", "")
            mobile = mobile.replace(")", "")
            mobile = mobile.replace("+45", "")
            if len(mobile) != 8:
                mobile_error.append(f"Fejl i {request.POST['inputGroupSelectMobile']}{row_count}: {mobile}")


        for index, row in df_excel_file.iterrows():
            mobile = row[inputGroupSelectMobile]
            first_name = row[inputGroupSelectFistName]
            last_name = row[inputGroupSelectLastName]




    return render(request, 'sms_app/import.html', {'form': form})