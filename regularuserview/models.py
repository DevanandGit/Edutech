from django.db import models
from user.models import RegularUserModel, FieldOfStudy
from exam.models import Exam
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(RegularUserModel, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    purchased_courses = models.ManyToManyField(FieldOfStudy, blank=True)
    purchased_exams = models.ManyToManyField(Exam, blank=True)

    def __str__(self) -> str:
        return f"{self.user}"
    
class PurchasedDate(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='purchasedate')
    date_of_purchase = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField()

# class PurchasedCourse(models.Model):
#     user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     course = models.ManyToManyField(FieldOfStudy, blank=True)
#     date_of_purchase = models.DateTimeField(default=timezone.now)

class UserResponse(models.Model):
    userprofile = models.OneToOneField(RegularUserModel, on_delete=models.CASCADE, related_name='userresponse')
    exam_id = models.CharField(max_length=50, unique=True)
    response = models.JSONField(default=dict)
    # {
    # "1": "A",
    # "2": "C",
    # "3": "B"
    # }
    marks_scored = models.CharField(max_length=4, default='00')

    def __str__(self) -> str:
        return f"{self.userprofile}"
