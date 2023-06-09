# Generated by Django 4.1.7 on 2023-07-01 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_alter_exam_duration_of_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='duration_of_exam',
            field=models.CharField(help_text='Enter the duration in the format "HH:MM:SS"', max_length=50),
        ),
        migrations.AlterField(
            model_name='exam',
            name='slug_exam',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='multiplechoice',
            name='slug_multiplechoice',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='multiselect',
            name='slug_multiselect',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='numericals',
            name='slug_numericals',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='slug_options',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='questiontype',
            name='slug_question_type',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
