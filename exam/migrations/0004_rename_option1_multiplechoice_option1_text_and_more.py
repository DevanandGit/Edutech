# Generated by Django 4.1.7 on 2023-07-29 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_alter_multiplechoice_question_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multiplechoice',
            old_name='option1',
            new_name='option1_text',
        ),
        migrations.RenameField(
            model_name='multiplechoice',
            old_name='option2',
            new_name='option2_text',
        ),
        migrations.RenameField(
            model_name='multiplechoice',
            old_name='option3',
            new_name='option3_text',
        ),
        migrations.RenameField(
            model_name='multiplechoice',
            old_name='option4',
            new_name='option4_text',
        ),
        migrations.RemoveField(
            model_name='options',
            name='options',
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='option1_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='option2_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='option3_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='option4_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='solution_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='solution_text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='numericals',
            name='solution_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='numericals',
            name='solution_text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='options',
            name='options_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='options',
            name='options_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='options',
            name='solution_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='options',
            name='solution_text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
