# Generated by Django 4.1.7 on 2023-07-28 11:09

from django.db import migrations, models
import django.db.models.deletion
import exam.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_unique_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('exam_id', models.CharField(default='000000', max_length=50)),
                ('exam_name', models.CharField(max_length=100, unique=True)),
                ('instruction', models.TextField()),
                ('duration_of_exam', exam.models.CustomDurationField(default='02:30:00')),
                ('total_marks', models.PositiveIntegerField()),
                ('pass_mark', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, help_text='Make Sure to Set Active-state while creating.')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('slug_exams', models.SlugField(blank=True)),
                ('access_type', models.ForeignKey(default='paid', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='user.access_type')),
                ('module', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='user.modules')),
            ],
        ),
        migrations.CreateModel(
            name='MultiSelect',
            fields=[
                ('msq_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('question_no', models.IntegerField()),
                ('question', models.TextField(max_length=500, null=True)),
                ('question_image', models.ImageField(null=True, upload_to='images/')),
                ('positive_marks', models.FloatField(default=0.0)),
                ('negetive_mark', models.FloatField(default=0.0)),
                ('slug_multiselect', models.SlugField(blank=True)),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multiselect', to='exam.exam')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(max_length=50, unique=True)),
                ('slug_question_type', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('option_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('option_no', models.PositiveIntegerField()),
                ('options', models.CharField(max_length=100)),
                ('is_answer', models.BooleanField(default=False)),
                ('slug_options', models.SlugField(blank=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='exam.multiselect')),
            ],
        ),
        migrations.CreateModel(
            name='Numericals',
            fields=[
                ('nq_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('question_no', models.IntegerField()),
                ('question', models.TextField(max_length=500, null=True)),
                ('question_image', models.ImageField(null=True, upload_to='images/')),
                ('ans_min_range', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ans_max_range', models.DecimalField(decimal_places=2, max_digits=6)),
                ('answer', models.DecimalField(decimal_places=2, max_digits=6)),
                ('positive_marks', models.FloatField(default=0.0)),
                ('negetive_mark', models.FloatField(default=0.0)),
                ('slug_numericals', models.SlugField(blank=True)),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numericals', to='exam.exam')),
                ('question_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.questiontype')),
            ],
        ),
        migrations.AddField(
            model_name='multiselect',
            name='question_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.questiontype'),
        ),
        migrations.CreateModel(
            name='MultipleChoice',
            fields=[
                ('mcq_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('question_no', models.IntegerField()),
                ('question', models.TextField(max_length=500, null=True)),
                ('question_image', models.ImageField(null=True, upload_to='images/')),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('positive_marks', models.FloatField(default=0.0)),
                ('negetive_mark', models.FloatField(default=0.0)),
                ('answer', models.CharField(choices=[('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4')], max_length=1)),
                ('slug_multiplechoice', models.SlugField(blank=True)),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multiplechoice', to='exam.exam')),
                ('question_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.questiontype')),
            ],
        ),
    ]
