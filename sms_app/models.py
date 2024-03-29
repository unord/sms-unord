from django.db import models
from django.urls import reverse


class Message(models.Model):

    # Relationships


    # Fields
    user = models.CharField(max_length=30, null=True, blank=True)
    link_code = models.CharField(max_length=30)
    time_to_send = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    completed = models.BooleanField(null=True, blank=True)
    message = models.TextField(max_length=600)
    email = models.EmailField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    validated_by_email = models.BooleanField(null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("sms_app_Message_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("sms_app_Message_update", args=(self.pk,))



class Recipient(models.Model):

    # Relationships
    message = models.ForeignKey("sms_app.Message", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    first_name = models.CharField(max_length=60, null=True, blank=True)
    last_name = models.CharField(max_length=60, null=True, blank=True)
    mobile_number = models.TextField(max_length=11)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    sent = models.BooleanField(null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("sms_app_Recipient_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("sms_app_Recipient_update", args=(self.pk,))

