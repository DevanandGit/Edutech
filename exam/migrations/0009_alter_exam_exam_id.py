# Generated by Django 4.1.7 on 2023-07-02 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0008_exam_exam_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_id',
            field=models.CharField(default='000000', max_length=150, null=True, unique=True),
        ),
    ]
