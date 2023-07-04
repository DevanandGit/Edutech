from django.db import models
from django.utils.text import slugify
from user.models import ActiveFieldManager,Access_type
#Three types of Question-(multiple choice, multiselect, numericals)
class QuestionType(models.Model):
    question_type = models.CharField(max_length=50, unique=True)
    slug_question_type = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug_question_type:
            self.slug_question_type = slugify(self.question_type)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.question_type}"

#Model to save Exam
class Exam(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    access_type = models.ForeignKey(Access_type, on_delete=models.SET_DEFAULT, null=True, default="paid")
    exam_name = models.CharField(max_length=100, unique=True)
    exam_id = models.CharField(max_length=150, unique=True, null=True, default="000000")
    instruction = models.TextField()
    duration_of_exam = models.CharField(max_length = 50,help_text='Enter the duration in the format "HH:MM:SS"')
    total_marks = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True, help_text="Make Sure to Set Active-state while creating.")
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date =  models.DateTimeField(auto_now=True, blank=True)
    slug_exam = models.SlugField(blank=True, unique=True)

    #Customised manager object
    objects = ActiveFieldManager()

    def save(self, *args, **kwargs):
        if not self.slug_exam:
            self.slug_exam = slugify(self.exam_name)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.exam_name}"

#Model to add Multiplechoice questions
#Options are need to enter and correct answer can be choosen within this model
class MultipleChoice(models.Model):
    question_type = models.ForeignKey(QuestionType, on_delete=models.SET_DEFAULT, default='MultipleChoice')
    exam_name = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='multiplechoice')
    question_no = models.IntegerField(unique=True)
    question = models.TextField(max_length=500, null=True)
    question_image = models.ImageField(upload_to='images/', null=True)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    marks = models.PositiveIntegerField(default=0)
    choose = (('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4'))
    answer = models.CharField(max_length=1, choices=choose)
    slug_multiplechoice = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug_multiplechoice:
            self.slug_multiplechoice = slugify(self.question_no)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.question}"

# # Model to add MultiSelect Question
class MultiSelect(models.Model): 
    id = models.AutoField(primary_key=True, unique=True)
    question_type = models.ForeignKey(QuestionType, on_delete=models.SET_DEFAULT, default='Multiselect')
    exam_name = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='multiselect')
    question_no = models.IntegerField(unique=True)
    question = models.TextField(max_length=500,null=True)
    question_image = models.ImageField(upload_to='images/', null=True)
    marks = models.PositiveIntegerField(default=0)
    slug_multiselect = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug_multiselect:
            self.slug_multiselect= slugify(self.question_no)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.question}"


#model to add options to Multiselect Question Type
class Options(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    question = models.ForeignKey(MultiSelect, on_delete=models.CASCADE, related_name='options')
    option_no = models.PositiveIntegerField(unique=True)
    options = models.CharField(max_length=100)
    is_answer = models.BooleanField(default=False)
    slug_options = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug_options:
            self.slug_options= slugify(self.option_no)
        return super().save(*args, **kwargs)

#model to add Numerical questions
class Numericals(models.Model):
    question_type = models.ForeignKey(QuestionType, on_delete=models.SET_DEFAULT, default='Numericals')
    exam_name = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='numericals')
    question_no = models.IntegerField(unique=True)
    question = models.TextField(max_length=500,null=True)
    question_image = models.ImageField(upload_to='images/', null=True)
    ans_min_range = models.DecimalField(max_digits=6,decimal_places=2)
    ans_max_range = models.DecimalField(max_digits=6,decimal_places=2)
    answer = models.DecimalField(max_digits=6,decimal_places=2)
    slug_numericals = models.SlugField(blank=True, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug_numericals:
            self.slug_numericals= slugify(self.question_no)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.question}"
    

#structure used here is 
"""  
            ACCESSTYPE(paid or free)
                |
              EXAM    QUESTION_TYPE             --PARENTS
                |           |
    (MULTIPLECHOICE, MULTISELECT, NUMERICALS)  --CHILDRENS
        |                 |            |
contains multiple-   contains mu-   contain numerical
choice questions    select ques     questions    
"""