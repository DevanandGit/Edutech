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
        fields = ['purchased_courses','purchased_exams']
    
    def get_purchased_courses(self, obj):
        # Get all the purchased courses related to the UserProfile
        purchased_courses = obj.purchased_courses.all()

        # Create a list of purchased courses with the date of purchase
        serialized_purchased_courses = []
        for course in purchased_courses:
            # Retrieve the corresponding PurchasedDate instance for each course
            purchased_date = PurchasedDate.objects.filter(user_profile=obj, user_profile__purchased_courses=course).first()

            # Check if there is a valid PurchasedDate instance for the course
            if purchased_date:
                serialized_purchased_courses.append({
                    'course_id': course.course_unique_id,
                    'date_of_purchase': purchased_date.date_of_purchase,
                    'expiration_date': purchased_date.expiration_date,
                })

        return serialized_purchased_courses
    
    def get_purchased_exams(self, obj):
        # Get all the purchased exams related to the UserProfile
        purchased_exams = obj.purchased_exams.all()

        # Create a list of dictionaries containing the exam details, including the date of purchase
        serialized_purchased_exams = []
        for exams in purchased_exams:
            purchased_date = PurchasedDate.objects.filter(user_profile=obj, user_profile__purchased_exams=exams).first()
            if purchased_date:
                serialized_purchased_exams.append({
                    'exam_id': exams.exam_unique_id,
                    'date_of_purchase': purchased_date.date_of_purchase,
                    'expiration_date': purchased_date.expiration_date,
                })

        return serialized_purchased_exams
    

class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = ['exam_id','response','marks_scored']

class DurationSerializer(serializers.Serializer):
    duration = serializers.IntegerField(min_value = 1, help_text="Enter duration in Months")