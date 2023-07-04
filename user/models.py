from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.text import slugify
from datetime import date
from django.core.exceptions import ValidationError
# from regularuserview.models import PurchasedCourses
#validate whether phone number is valid
phone_regex = RegexValidator(
    regex=r'^\d{10}$',
    message="Phone number must be 10 digits."
)
#manager overriden.
class ActiveFieldManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    


#select the field of studies from class FieldOfStudy.
#Add Course instances.
class FieldOfStudy(models.Model): #parent
    id = models.AutoField(unique=True, primary_key=True)
    field_of_study = models.CharField(max_length=200, unique=True)
    course_image = models.ImageField(upload_to='images/', null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=100)
    Course_description = models.TextField(default="course Description")
    user_benefit = models.TextField(help_text="Enter what the user's benefit with the course.", default="user benefits")
    slug_studyfield = models.SlugField(blank=True, unique=True)
    is_active = models.BooleanField(default=True, help_text="Make Sure to Set Active-state while creating.")
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date =  models.DateTimeField(auto_now=True, blank=True)

    #Customised manager object
    objects = ActiveFieldManager()

    def save(self, *args, **kwargs):
        if not self.slug_studyfield:
            self.slug_studyfield = slugify(self.field_of_study)
        return super().save(*args, **kwargs) 

    def __str__(self) -> str:
        return f"course name:{self.field_of_study}"

#overriden user model.
class RegularUserModel(AbstractUser):
    name = models.CharField(max_length=100)
    username = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, validators=[phone_regex])
    purhcased_course = models.ManyToManyField(FieldOfStudy, blank=True)
    USERNAME_FIELD = 'username'
    

#can add the all available teachers.
class Teachers(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    teachers = models.CharField(max_length=200)
    slug_teachers = models.SlugField(blank=True, unique=True)
    is_active = models.BooleanField(default=True, blank=True, help_text="Make Sure to Set Active-state while creating.")
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date =  models.DateTimeField(auto_now=True, blank=True)

    objects = ActiveFieldManager()

    def save(self, *args, **kwargs):
        if not self.slug_teachers:
            self.slug_teachers = slugify(self.teachers)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Teacher name:{self.teachers}"

#store all the subjects.
class Subjects(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    field_of_study = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE, related_name='subjects') #FieldOfStudy = parent of subjects.
    subject_image = models.ImageField(upload_to='images/', null=True)
    subjects = models.CharField(max_length=200, unique=True)
    taught_by = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True)
    slug_subjects = models.SlugField(blank=True, unique=True)
    is_active = models.BooleanField(default=True, help_text="Make Sure to Set Active-state while creating.")
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date =  models.DateTimeField(auto_now=True, blank=True)

    #Customised manager object
    objects = ActiveFieldManager()

    def save(self, *args, **kwargs):
        if not self.slug_subjects:
            self.slug_subjects = slugify(self.subjects)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"subjects:{self.subjects} taught by: {self.taught_by}"

#model to add modules of subjects.
class Modules(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='modules') #Subject = parent of modules 
    module_no = models.IntegerField(unique=True) 
    module_name = models.CharField(max_length=400)
    slug_modules = models.SlugField(blank=True, unique=True)
    is_active = models.BooleanField(default=True, help_text="Make Sure to Set Active-state while creating.")
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date =  models.DateTimeField(auto_now=True, blank=True)

    #Customised manager object.
    objects = ActiveFieldManager()

    def save(self, *args, **kwargs):
        if not self.slug_modules:
            self.slug_modules = slugify(self.module_no)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"module no:{self.module_no} module name: {self.module_name}"

#model to add the access type (paid or free)
class Access_type(models.Model):
    access_type = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return f"{self.access_type}"
    
class NotesNested(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    module = models.ForeignKey(Modules, on_delete=models.CASCADE, related_name="notes") #Modules = parent of Notes
    access_type = models.ForeignKey(Access_type, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #To store the title of note,
    description = models.TextField(max_length=600, blank=True) #To store the description of notes 
    pdf_link = models.URLField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date =  models.DateTimeField(auto_now=True, blank=True)
    slug_notes = models.SlugField(blank=True, unique=True)
    is_active = models.BooleanField(default=True, help_text="Make Sure to Set Active-state while creating.")
    
    #Customised manager object
    objects = ActiveFieldManager()

    def save(self, *args, **kwargs):
        if not self.slug_notes:
            self.slug_notes = slugify(self.id)
        return super().save(*args, **kwargs)

class ExamsNested(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    module = models.ForeignKey(Modules, on_delete=models.CASCADE, related_name="exams") #Modules = parent of Exams
    access_type = models.ForeignKey(Access_type, on_delete=models.CASCADE)
    exam_id = models.CharField(max_length=50, unique=True) 
    title = models.CharField(max_length=200) #To store the title exam.
    description = models.TextField(max_length=600, blank=True) #To store the description of exam 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date =  models.DateTimeField(auto_now=True)
    slug_exams = models.SlugField(blank=True, unique=True)
    is_active = models.BooleanField(default=True, help_text="Make Sure to Set Active-state while creating.")
    
    #Customised manager object
    objects = ActiveFieldManager()

    def save(self, *args, **kwargs):
        if not self.slug_exams:
            self.slug_exams = slugify(self.exam_id)
        return super().save(*args, **kwargs)
    
class videosNested(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    module = models.ForeignKey(Modules, on_delete=models.CASCADE, related_name="videos") #Modules = parent of  video.
    access_type = models.ForeignKey(Access_type, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=50, unique=True) 
    title = models.CharField(max_length=200) #To store the title video
    description = models.TextField(max_length=600, blank=True) #To store the description of video
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date =  models.DateTimeField(auto_now=True)
    slug_videos = models.SlugField(blank=True, unique=True)
    is_active = models.BooleanField(default=True, help_text="Make Sure to Set Active-state while creating.")
    
    #Customised manager object
    objects = ActiveFieldManager()

    def save(self, *args, **kwargs):
        if not self.slug_videos:
            self.slug_videos = slugify(self.video_id)
        return super().save(*args, **kwargs)

