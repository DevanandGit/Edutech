# Generated by Django 4.1.7 on 2023-09-04 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='otp_validated',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
