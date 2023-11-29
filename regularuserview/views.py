from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView, RetrieveAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from user.models import (FieldOfStudy, Subjects,
                         Modules,RegularUserModel,
                         videosNested, NotesNested, 
                         SliderImage, PopularCourses)
from user.serializers import (FieldOfStudySerializer, SubjectSerializer, ModuleSerializer,
                              RegularUserSerializer, VideoNestedSerializer,
                              NotesNestedSerializer, SliderImageSerializer, PopularCourseSerializer)
from .serializer import UserResponseSerializer, UserProfileSerializer, PurchasedDateSerializer, DurationSerializer
from exam.models import Exam
from exam.serializer import ExamSerializer
from .models import UserProfile,UserResponse, PurchasedDate
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from django.db.models import Q
from rest_framework.pagination import LimitOffsetPagination
#course List
class CoursesList(ListAPIView):
    queryset = FieldOfStudy.objects.filter(is_active = True)
    serializer_class = FieldOfStudySerializer

#Course DetailView
class CoursesRetrieveView(RetrieveAPIView):
    queryset = FieldOfStudy.objects.all()
    serializer_class = FieldOfStudySerializer
    lookup_field = 'course_unique_id'

#subjects List view
class SubjectsList(ListAPIView):
    serializer_class = SubjectSerializer
    lookup_field = 'course_unique_id'

    def get_queryset(self):
        course_unique_id = self.kwargs['course_unique_id']
        course = FieldOfStudy.objects.get(course_unique_id = course_unique_id)
        return course.subjects.filter(is_active = True)

#subjects Detail view
class SubjectsRetrieveView(RetrieveAPIView):
    queryset = Subjects.objects.filter(is_active = True)
    serializer_class = SubjectSerializer
    lookup_field = 'subject_id'

#Modules List view
class ModulesList(ListAPIView):
    serializer_class = ModuleSerializer
    lookup_field = 'subject_id'

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        subjects = Subjects.objects.get(subject_id = subject_id)
        return subjects.modules.filter(is_active = True)

#Modules Detail view
class ModulesRetrieveView(RetrieveAPIView):
    queryset = Modules.objects.filter(is_active = True)
    serializer_class = ModuleSerializer
    lookup_field = 'modules_id'
    
#list and write exams inside of the course
class ExamsNestedListView(ListAPIView):
    serializer_class = ExamSerializer
    lookup_field = "modules_id"
    def get_queryset(self):
        modules_id = self.kwargs["modules_id"] #extract 'modules_id'
        modules = Modules.objects.get(modules_id = modules_id)   #extract modules based on that 'modules_id'
        return modules.exams.filter(is_active = True)  #extract all exams based on that 'modules_id'
#Exams inside Modules Detailview
class ExamsNestedDetailView(RetrieveAPIView):
    queryset = Exam.objects.filter(is_active = True)
    serializer_class = ExamSerializer
    lookup_field = "exam_unique_id"

#list and write videos
class videosNestedListView(ListAPIView):
    serializer_class = VideoNestedSerializer
    lookup_field = "modules_id"

    def get_queryset(self):
        modules_id = self.kwargs["modules_id"] #extract 'modules_id'
        modules = Modules.objects.get(modules_id = modules_id)  #extract modules based on that 'modules_id'
        return modules.videos.filter(is_active = True)   #extract all videos based on that 'modules_id'

#Videos inside Modules Detailview
class VideosNestedDetailView(RetrieveAPIView):
    queryset = videosNested.objects.filter(is_active = True)
    serializer_class = VideoNestedSerializer
    lookup_field = "video_unique_id"

#list and write notes
class NotesNestedListView(ListAPIView):
    serializer_class = NotesNestedSerializer
    lookup_field = "modules_id"

    def get_queryset(self):
        modules_id = self.kwargs["modules_id"]  #extract 'modules_id'
        modules = Modules.objects.get(modules_id = modules_id)  #extract modules based on that 'modules_id'
        return modules.notes.filter(is_active = True) #extract all notes based on that 'modules_id'

#Videos inside Modules Detailview
class NotesNestedDetailView(RetrieveAPIView):
    queryset = NotesNested.objects.filter(is_active = True)
    serializer_class = NotesNestedSerializer
    lookup_field = "notes_id"

#List all available exams.
class ExamListView(ListAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()

#retrieve exams according to examid as slug
class ExamRetrieveView(RetrieveAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.filter(is_active = True)
    lookup_field = 'exam_unique_id'

class BuyExam(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, exam_unique_id):
        try:
            exam = Exam.objects.get(exam_unique_id=exam_unique_id)
        except Exam.DoesNotExist:
            return Response("Exam not found", status=status.HTTP_404_NOT_FOUND)

        duration = int(request.data.get('duration')) #duration in days
        
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        date_of_purchase = timezone.now()
        expiration_date = date_of_purchase + timezone.timedelta(days=duration)

        user_profile.purchased_exams.add(exam)

        purchased_date = PurchasedDate.objects.create(user_profile=user_profile, 
                                                      exam=exam,
                                                      date_of_purchase=date_of_purchase,
                                                      expiration_date=expiration_date)
        return Response("Exam purchased successfully", status=status.HTTP_200_OK)

class BuyCourse(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, course_unique_id):
        try:
            course = FieldOfStudy.objects.get(course_unique_id=course_unique_id)
        except FieldOfStudy.DoesNotExist:
            return Response("Course not found", status=status.HTTP_404_NOT_FOUND)

        duration = int(request.data.get('duration')) #duration in days

        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        date_of_purchase = timezone.now()
        expiration_date = date_of_purchase + timezone.timedelta(days=duration)

        user_profile.purchased_courses.add(course)

        purchased_date = PurchasedDate.objects.create(user_profile=user_profile,
                                                      course=course,
                                                      date_of_purchase=date_of_purchase,
                                                      expiration_date=expiration_date)

        return Response("Course purchased successfully", status=status.HTTP_200_OK)
#view to add ExamResponse of User.
class UserExamResponseAdd(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        serializer = UserResponseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        exam_id = validated_data.get('exam_id')
        response_data = validated_data.get('response')
        marks_scored = validated_data.get('marks_scored', '00')
        
        try:
            user_response = UserResponse.objects.create(
                user=user,
                exam_id=exam_id,
                response=response_data,
                marks_scored=marks_scored,
            )

            response = {
                "message": "User response added successfully",
                'data': {
                    'exam_id': exam_id,
                    'response': response_data,
                    'marks_scored': marks_scored,
                },
                'status': status.HTTP_201_CREATED
            }
            return Response(response, status=status.HTTP_201_CREATED)

        except:
            return Response("User not found", status=status.HTTP_401_UNAUTHORIZED)

#User Profile View.
class UserProfileView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = RegularUserSerializer
    lookup_field = 'username'
    def get_queryset(self):
        # Only allow the user to access their own instance
        return RegularUserModel.objects.filter(username=self.request.user.username)

#show the purchased history.
class PurchaseHistoryView(ListAPIView):
    serializer_class = UserProfileSerializer
    lookup_field = 'username'
    def get_queryset(self): 
        return UserProfile.objects.filter(user = self.request.user)

class SliderImageView(ListAPIView):
    serializer_class = SliderImageSerializer
    queryset = SliderImage.objects.all()

class PopularCourseView(ListAPIView):
    serializer_class = PopularCourseSerializer
    queryset = PopularCourses.objects.all()


class UserResponses(ListAPIView):
    # pagination_class = LimitOffsetPagination
    # permission_classes = [IsAdminUser]
    serializer_class = UserResponseSerializer
    queryset = UserResponse.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['exam_id', 'exam_name','user__username']

    def get_queryset(self):
        queryset = super().get_queryset()
        # Apply search filtering
        search_query = self.request.query_params.get('search')
        if search_query:
            # Split the search query into individual words and create a Q object for each word
            search_words = search_query.split()
            search_filter = Q()
            for word in search_words:
                search_filter |= (Q(exam_id__icontains=word) | Q(user__username__icontains=word))
                                  
            queryset = queryset.filter(search_filter)

        return queryset
