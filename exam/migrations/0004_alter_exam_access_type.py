# Generated by Django 4.1.7 on 2023-07-01 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('exam', '0003_multiselect_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='access_type',
            field=models.ForeignKey(default='paid', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='user.access_type'),
        ),
    ]
