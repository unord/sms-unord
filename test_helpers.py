import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from sms_app import models as sms_app_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_sms_app_Message(**kwargs):
    defaults = {}
    defaults["link_code"] = ""
    defaults["time_to_send"] = datetime.now()
    defaults["completed"] = ""
    defaults["message"] = ""
    if "user" not in kwargs:
        defaults["user"] = create_User()
    defaults.update(**kwargs)
    return sms_app_models.Message.objects.create(**defaults)
def create_sms_app_Recipient(**kwargs):
    defaults = {}
    defaults["mobile_number"] = ""
    defaults["first_name"] = ""
    defaults["sent"] = ""
    defaults["last_name"] = ""
    if "message" not in kwargs:
        defaults["message"] = create_sms_app_Message()
    defaults.update(**kwargs)
    return sms_app_models.Recipient.objects.create(**defaults)