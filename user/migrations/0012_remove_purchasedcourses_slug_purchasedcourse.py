# Generated by Django 4.1.7 on 2023-07-03 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_purchasedcourses_regularusermodel_purhcased_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasedcourses',
            name='slug_purchasedcourse',
        ),
    ]
