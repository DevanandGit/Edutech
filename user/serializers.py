from rest_framework import serializers
from .models import RegularUserModel
from django.contrib.auth import get_user_model
from .models import (FieldOfStudy,
                    Subjects, Modules, 
                    Access_type, NotesNested, 
                    videosNested, SliderImage, PopularCourses)
from regularuserview.serializer import UserProfileSerializer, UserResponseSerializer
# from regularuserview.serializer import PurchasedCourseSerializer
RegularUserModel = get_user_model()

#validate data of regular user Registration.
class RegularUserSerializer(serializers.ModelSerializer):
    password = serializers.RegexField(
            regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
            max_length=128,
            min_length=8,
            write_only=True,
            error_messages={
                'invalid': 'Password must contain at least 8 characters, including uppercase, lowercase, and numeric characters.'
            }   
        )
    confirm_password = serializers.CharField(write_only=True)
    purchase_list = UserProfileSerializer(source='user', read_only =True)
    exam_response = UserResponseSerializer(source= 'userresponse', read_only = True)
    class Meta:
        model = RegularUserModel
        fields = ['id','name', 'username', 'phone_number', 'password', 'confirm_password','date_joined','last_login','is_active','purchase_list','exam_response']
        default_related_name = 'regular_users'

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Password mismatch')
        return data
        
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = RegularUserModel.objects.create_user(
            name = validated_data['name'],
            username = validated_data['username'],
            phone_number = validated_data['phone_number'],
            password = validated_data['password']
            )
        return user

#validate data of regular user login.
class RegularUserLoginSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField(max_length=128)

#validate data for admin creation.
class AdminRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.RegexField(
        regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
        max_length=128,
        min_length=8,
        write_only=True,
        error_messages={
            'invalid': 'Password must contain at least 8 characters, including uppercase, lowercase, and numeric characters.'
        }
    )
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = RegularUserModel
        fields = ['name', 'username', 'password', 'confirm_password']
        default_related_name = 'admin_users'

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Password mismatch')
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = RegularUserModel.objects.create_superuser(
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data['name']
        )
        return user

#validate data for admin login.
class AdminLoginSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField(max_length=128)

# #validate teacher data
# class TeachersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Teachers
#         fields = ['id', 'teachers','slug_teachers','is_active', 'created_date', 'updated_date']


#validates Notes nested inside Modules.
class NotesNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesNested
        fields = ['notes_id','module','access_type','title','description','pdf_link','created_date','updated_date','slug_notes','is_active']

#validates Videos nested inside Modules.
class VideoNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = videosNested
        fields = ['video_unique_id','module','access_type','video_id','title','description','created_date','updated_date','slug_videos','is_active']

#validate modules data
class ModuleSerializer(serializers.ModelSerializer):
    contents_count = serializers.SerializerMethodField()
    notes = serializers.StringRelatedField(many=True)
    videos = serializers.StringRelatedField(many=True)
    exams = serializers.StringRelatedField(many=True)
    class Meta:
        model = Modules
        fields = ['modules_id', 'subjects','module_name', 'contents_count', 'notes', 'videos', 'exams','slug_modules','is_active', 'created_date', 'updated_date']
    
    def get_contents_count(self, obj):
        return (obj.notes.count()+obj.videos.count()+obj.exams.count())

#validates subjects data
class SubjectSerializer(serializers.ModelSerializer):
    modules_count = serializers.SerializerMethodField()
    modules = serializers.StringRelatedField(many=True)
    class Meta:
        model = Subjects
        fields = ['subject_id','field_of_study','subjects','subject_image', 'modules_count','modules','slug_subjects','direct_slug','is_active', 'created_date', 'updated_date']
    
    def get_modules_count(self, obj):
        return obj.modules.count()

#validates Field of study data
class FieldOfStudySerializer(serializers.ModelSerializer):
    subjects_count = serializers.SerializerMethodField()
    subjects = serializers.StringRelatedField(many=True)
    class Meta:
        model = FieldOfStudy
        fields = ['course_unique_id','field_of_study', 'course_image','cover_image','price', 'Course_description','user_benefit','only_paid','subjects_count','subjects','slug_studyfield','is_active', 'created_date', 'updated_date']

    def get_subjects_count(self, obj):
        return obj.subjects.count()


#validates the access types(paid or free)
class Access_type_serializer(serializers.ModelSerializer):
    class Meta:
        model = Access_type
        fields = "__all__"

class SliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImage
        fields = ['images_id','images']

class PopularCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularCourses
        fields = ['popular_course_id','course']

