import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Message_list_view(client):
    instance1 = test_helpers.create_sms_app_Message()
    instance2 = test_helpers.create_sms_app_Message()
    url = reverse("sms_app_Message_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Message_create_view(client):
    user = test_helpers.create_User()
    url = reverse("sms_app_Message_create")
    data = {
        "completed": true,
        "message": "text",
        "email": "user@tempurl.com",
        "link_code": "text",
        "time_to_send": datetime.now(),
        "validated_by_email": true,
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Message_detail_view(client):
    instance = test_helpers.create_sms_app_Message()
    url = reverse("sms_app_Message_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Message_update_view(client):
    user = test_helpers.create_User()
    instance = test_helpers.create_sms_app_Message()
    url = reverse("sms_app_Message_update", args=[instance.pk, ])
    data = {
        "completed": true,
        "message": "text",
        "email": "user@tempurl.com",
        "link_code": "text",
        "time_to_send": datetime.now(),
        "validated_by_email": true,
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Recipient_list_view(client):
    instance1 = test_helpers.create_sms_app_Recipient()
    instance2 = test_helpers.create_sms_app_Recipient()
    url = reverse("sms_app_Recipient_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Recipient_create_view(client):
    message = test_helpers.create_sms_app_Message()
    url = reverse("sms_app_Recipient_create")
    data = {
        "last_name": "text",
        "mobile_number": "text",
        "sent": true,
        "first_name": "text",
        "message": message.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Recipient_detail_view(client):
    instance = test_helpers.create_sms_app_Recipient()
    url = reverse("sms_app_Recipient_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Recipient_update_view(client):
    message = test_helpers.create_sms_app_Message()
    instance = test_helpers.create_sms_app_Recipient()
    url = reverse("sms_app_Recipient_update", args=[instance.pk, ])
    data = {
        "last_name": "text",
        "mobile_number": "text",
        "sent": true,
        "first_name": "text",
        "message": message.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302