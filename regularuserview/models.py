from django.db import models
from user.models import RegularUserModel, FieldOfStudy
from exam.models import Exam
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(RegularUserModel, on_delete=models.CASCADE, related_name='user_profile', null=True, blank=True)
    purchased_courses = models.ManyToManyField(FieldOfStudy, blank=True, related_name='purchased_profiles')
    purchased_exams = models.ManyToManyField(Exam, blank=True, related_name='purchased_profiles')

    def __str__(self) -> str:
        return f"{self.user}"

class PurchasedDate(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='purchased_dates')
    course = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE, related_name='purchased_dates', null=True, blank=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='purchased_dates', null=True, blank=True)
    date_of_purchase = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField()

    def __str__(self) -> str:
        return f"PurchasedDate for {self.user_profile} - Course: {self.course}, Exam: {self.exam}"


# class PurchasedCourse(models.Model):
#     user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     course = models.ManyToManyField(FieldOfStudy, blank=True)
#     date_of_purchase = models.DateTimeField(default=timezone.now)

class UserResponse(models.Model):
    user = models.ForeignKey(RegularUserModel, on_delete=models.CASCADE, related_name='userresponse')
    exam_id = models.CharField(max_length=50)
    response = models.JSONField(default=dict)
    marks_scored = models.CharField(max_length=4, default='00')
    #  {
    # "1": "A",
    # "2": "C",
    # "3": "B"
    # }
    def __str__(self) -> str:
        return f"{self.userprofile.username}-{self.exam_id}"
