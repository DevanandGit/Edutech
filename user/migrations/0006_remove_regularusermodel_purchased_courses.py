# Generated by Django 4.1.7 on 2023-07-02 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_regularusermodel_purchased_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regularusermodel',
            name='purchased_courses',
        ),
    ]
