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
        file = request.FILES['file']
        df_excel_file = pd.read_excel(file, header=None)
        print(df_excel_file)
        username = request.POST['username']
        inputGroupSelectMobile = letters_to_numbers(str(request.POST['inputGroupSelectMobile']))-1
        inputGroupSelectFistName = letters_to_numbers(str(request.POST['inputGroupSelectFistName']))-1
        inputGroupSelectLastName = letters_to_numbers(str(request.POST['inputGroupSelectLastName']))-1

        df_to_analyze = df_excel_file[[inputGroupSelectMobile]]
        if inputGroupSelectFistName != 99:
            df_to_analyze[1] = df_excel_file[inputGroupSelectFistName]
        else:
            df_to_analyze[1] = ""

        if inputGroupSelectLastName != 99:
            df_to_analyze[2] = df_excel_file[inputGroupSelectLastName]
        else:
            df_to_analyze[2] = ""



        print(df_to_analyze)

        #message = request.POST['message']
        #sms_send = request.POST['sms_send']

        mobile_error = []
        row_count = 0
'''
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


       # for index, row in df_excel_file.iterrows():
       #     mobile = row[inputGroupSelectMobile]
       #     first_name = row[inputGroupSelectFistName]
       #     last_name = row[inputGroupSelectLastName]

'''
        #return render(request, 'sms_app/upload_sms_list.html', {'mobile_error': mobile_error})


def letters_to_numbers(letter: str) -> int:
    if letter == "99":
        return 99
    elif letter.upper() == "A":
        return 1
    elif letter.upper() == "B":
        return 2
    elif letter.upper() == "C":
        return 3
    elif letter.upper() == "D":
        return 4
    elif letter.upper() == "E":
        return 5
    elif letter.upper() == "F":
        return 6
    elif letter.upper() == "G":
        return 7
    elif letter.upper() == "H":
        return 8
    elif letter.upper() == "I":
        return 9
    elif letter.upper() == "J":
        return 10
    elif letter.upper() == "K":
        return 11
    elif letter.upper() == "L":
        return 12
    elif letter.upper() == "M":
        return 13
    elif letter.upper() == "N":
        return 14
    elif letter.upper() == "O":
        return 15
    elif letter.upper() == "P":
        return 16
    elif letter.upper() == "Q":
        return 17
    elif letter.upper() == "R":
        return 18
    elif letter.upper() == "S":
        return 19
    elif letter.upper() == "T":
        return 20
    elif letter.upper() == "U":
        return 21
    elif letter.upper() == "V":
        return 22
    elif letter.upper() == "W":
        return 23
    elif letter.upper() == "X":
        return 24
    elif letter.upper() == "Y":
        return 25
    elif letter.upper() == "Z":
        return 26

