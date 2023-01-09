# Generated by Django 4.1.1 on 2023-01-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='validated_by_email',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]