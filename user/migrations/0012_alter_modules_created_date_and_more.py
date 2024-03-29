# Generated by Django 4.1.7 on 2023-08-31 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_modules_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modules',
            name='created_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='modules',
            name='updated_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='notesnested',
            name='created_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='notesnested',
            name='updated_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='videosnested',
            name='created_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='videosnested',
            name='updated_date',
            field=models.DateTimeField(),
        ),
    ]
