from rest_framework import serializers
from .models import UserProfile, UserResponse, PurchasedDate

class PurchasedDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedDate
        fields = ['date_of_purchase','expiration_date']


class UserProfileSerializer(serializers.ModelSerializer):
    purchased_courses = serializers.SerializerMethodField()
    purchased_exams = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['purchased_courses', 'purchased_exams']

    def get_purchased_courses(self, obj):
        purchased_dates = obj.purchased_dates.filter(course__isnull=False)
        serialized_purchased_courses = []
        for purchased_date in purchased_dates:
            serialized_purchased_courses.append({
                'course_id': purchased_date.course.course_unique_id,
                'date_of_purchase': purchased_date.date_of_purchase,
                'expiration_date': purchased_date.expiration_date,
            })
        return serialized_purchased_courses

    def get_purchased_exams(self, obj):
        purchased_dates = obj.purchased_dates.filter(exam__isnull=False)
        serialized_purchased_exams = []
        for purchased_date in purchased_dates:
            serialized_purchased_exams.append({
                'exam_id': purchased_date.exam.exam_unique_id,
                'date_of_purchase': purchased_date.date_of_purchase,
                'expiration_date': purchased_date.expiration_date,
            })
        return serialized_purchased_exams


class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = ['exam_id','exam_name','response','qualify_score','time_taken','marks_scored']

class DurationSerializer(serializers.Serializer):
    duration = serializers.IntegerField(min_value = 1, help_text="Enter duration in Months")