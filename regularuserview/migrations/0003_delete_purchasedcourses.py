# Generated by Django 4.1.7 on 2023-07-03 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regularuserview', '0002_purchasedcourses_slug_purchasedcourse'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PurchasedCourses',
        ),
    ]
