# Generated by Django 4.1.7 on 2023-08-01 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_notesnested_pdf_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notesnested',
            old_name='pdf_link',
            new_name='pdf',
        ),
    ]
