# Generated by Django 4.1.7 on 2023-07-28 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_name',
            field=models.CharField(max_length=100),
        ),
    ]
