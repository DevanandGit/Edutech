# Generated by Django 4.1.7 on 2023-07-03 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regularuserview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedcourses',
            name='slug_purchasedcourse',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
