from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms
import pandas as pd
import random
import string
from . import unord_mail
from . import unord_sms


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
    if request.method == 'POST':
        file = request.FILES['file']
        df_excel_file = pd.read_excel(file, header=None)
        email = request.POST['username']+'@unord.dk'
        message = request.POST['message']
        time_to_send = request.POST['sms_send']
        link_code = generate_random_string(16)
        user = request.user


        inputGroupSelectMobile = letters_to_numbers(str(request.POST['inputGroupSelectMobile']))-1
        try:
            inputGroupSelectFistName = letters_to_numbers(str(request.POST['inputGroupSelectFistName']))-1
        except:
            inputGroupSelectFistName = 99
        try:
            inputGroupSelectLastName = letters_to_numbers(str(request.POST['inputGroupSelectLastName']))-1
        except:
            inputGroupSelectLastName = 99

        df_to_analyze = df_excel_file[[inputGroupSelectMobile]].astype('string')
        if inputGroupSelectFistName != 99:
            df_to_analyze[1] = df_excel_file[inputGroupSelectFistName]
        else:
            df_to_analyze[1] = ""

        if inputGroupSelectLastName != 99:
            df_to_analyze[2] = df_excel_file[inputGroupSelectLastName]
        else:
            df_to_analyze[2] = ""

        df_to_analyze.rename(columns={1: 'mobile', 2: 'first_name', 3: 'last_name'}, inplace = True)

        mobile_error = []
        row_count = 0
        # loop through df_to_analyze['mobile'] and check if string only contains numbers
        for index, row in df_to_analyze.iterrows():
            row_count += 1
            org_value = row['mobile']
            row['mobile'] = row['mobile'].replace(" ", "")
            row['mobile'] = row['mobile'].replace("-", "")
            row['mobile'] = row['mobile'].replace("(", "")
            row['mobile'] = row['mobile'].replace(")", "")
            row['mobile'] = row['mobile'].replace("+45", "")

            if not row['mobile'].isnumeric():
                mobile_error.append(f"Fejl i telefon nummer række:{request.POST['inputGroupSelectMobile']}{row_count}. Værdi: {org_value}")

        if len(mobile_error) > 0:
            print(df_to_analyze)
            return render(request, 'sms_app/upload_sms_list_error.html', {'mobile_error': mobile_error})

        #add record to model Message and add df_to_analyze to model Recipient that belongs to Message
        message = models.Message.objects.create(email=email, message=message, link_code=link_code, time_to_send=time_to_send, user=user)

        #loop through df_to_analyze and add each row to model Recipient matching the Message
        for index, row in df_to_analyze.iterrows():
            models.Recipient.objects.create(message=message, mobile_number=row['mobile'], first_name=row['first_name'], last_name=row['last_name'])

        email_from = 'helpdesk@unord.dk'
        recipient_list = [email,]
        email_subject = 'SMS liste upload skal godkendes'
        email_body= f"Vi har modtaget en sms liste fra {email} med link: https://sms.unord.dk/sms_app/recipient_list/{link_code}/"
        unord_mail.send_email_with_attachments(email_from, recipient_list, email_subject, email_body, [], [], [])

        return render(request, 'sms_app/upload_sms_list_success.html', {'message': message})


def generate_random_string(n):
  # Get a random selection of letters and digits
  choices = string.ascii_letters + string.digits

  # Use ''.join() to convert the sequence of characters to a string
  return ''.join(random.choices(choices, k=n))

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

