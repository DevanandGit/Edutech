# Generated by Django 4.1.7 on 2023-07-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_regularusermodel_purchased_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='regularusermodel',
            name='purchased_courses',
            field=models.ManyToManyField(blank=True, to='user.fieldofstudy'),
        ),
    ]
