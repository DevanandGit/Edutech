from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.utils import timezone
from .models import (Access_type,
                    FieldOfStudy, Subjects, Modules,
                     videosNested, NotesNested, RegularUserModel)
from .serializers import (RegularUserSerializer,RegularUserLoginSerializer,
                        AdminLoginSerializer, AdminRegistrationSerializer,
                        Access_type_serializer,FieldOfStudySerializer,
                        ModuleSerializer,SubjectSerializer,
                        VideoNestedSerializer, NotesNestedSerializer)
from regularuserview.models import UserProfile, PurchasedDate
from regularuserview.serializer import DurationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.generics import (CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                     ListAPIView,RetrieveUpdateDestroyAPIView)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework import status

class RegularUserRegisterationView(APIView):
    serializer_class = RegularUserSerializer
    def post(self, request):
        serializer = RegularUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = serializer.save()
            # Logging in the user after successful registration
            login(request, user)
            # Generating or retrieving the token for the logged-in user
            token, created = Token.objects.get_or_create(user=user)
            response = {
                'data': serializer.data,
                'token': token.key,
                'status': status.HTTP_201_CREATED
            }
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Regular User login view.
class RegularUserLoginView(APIView):
    serializer_class = RegularUserLoginSerializer

    def post(self, request):
        serializer = RegularUserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, username=serializer.data['username'], password=serializer.data['password'])
        if user is not None and not user.is_anonymous:
            # Invalidate all sessions except for the current one
            active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
            for session in active_sessions:
                session_data = session.get_decoded()
                if str(user.pk) == session_data.get('_auth_user_id'):
                    Token.objects.filter(user=user).delete()
                    session.delete()
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            print(token)
            response = {'message': 'Login Successful', 'token': token.key}
            return Response(response)
        
        return Response('The username or password is incorrect')

#Regular user logout view.

class RegularUserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Delete the token associated with the user
        Token.objects.filter(user=request.user).delete()
        logout(request)
        response = {'message': 'You have been successfully logged out.'}
        return Response(response)

#Admin Registration view.
class AdminRegistrationView(CreateAPIView):
    serializer_class = AdminRegistrationSerializer

#Admin Login View.
#Authentication using django default authentication system.
class AdminLoginView(APIView):
    serializer_class = AdminLoginSerializer
    def post(self, request):
        serializer = AdminLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = authenticate(request, username = serializer.data['username'], password = serializer.data['password'])
        if user is not None and user.is_superuser:
            login(request, user)
            response = {'message': 'Login Successful',}
            return Response(response)
        return Response('The username or password is incorrect')

#Admin Logout View.
#endpoint can only be accessed if the user has authentication permission.
class AdminLogoutView(APIView):
    
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if request.user.is_superuser:
            logout(request)
            response = {'message': 'You have been successfully logged out.'}
            return Response(response)
        else:
            return Response("invalid access")

# #Create Teachers view.
# class TeacherListCreateView(ListCreateAPIView):
#     permission_classes = [IsAdminUser]
#     queryset = Teachers.objects.all()
#     serializer_class = TeachersSerializer

# #Teacher Detailview.
# class TeacherRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAdminUser]
#     queryset = Teachers.objects.all()
#     serializer_class = TeachersSerializer


#create access type- (paid, free) view.
class AccessTypeListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Access_type.objects.all()
    serializer_class = Access_type_serializer

#AccessTypeDetailView
class AccessTypeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Access_type.objects.all()
    serializer_class = Access_type_serializer

#Course Overview view.
class FieldOfStudyListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = FieldOfStudy.objects.prefetch_related('subjects')
    serializer_class = FieldOfStudySerializer

#Course Detailview.
class FieldOfStudyRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = FieldOfStudy.objects.all()
    serializer_class = FieldOfStudySerializer
    lookup_field = "course_unique_id"

#Subjects overview view.
class SubjectsListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SubjectSerializer
    lookup_field = "course_unique_id"

    def get_queryset(self):
        course_unique_id = self.kwargs['course_unique_id']  #extract all 'course_unique_id'
        field_of_study = FieldOfStudy.objects.get(course_unique_id=course_unique_id) #extract FieldOfStudy objects based on that 'course_unique_id'
        return field_of_study.subjects.all() #extract all subjects associated with that 'study_slugfield'

#Subjects Detailview View.
class SubjectsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = "subject_id"

#Modules OverView View.
class ModulesListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ModuleSerializer
    lookup_field = "subject_id"

    def get_queryset(self):
        subject_id = self.kwargs["subject_id"]  #extract all 'slug_subjects'
        subjects = Subjects.objects.get(subject_id = subject_id)  #extract all subjects based on that 'slug_subjects'
        return subjects.modules.all()  #extract all modules based on that 'study_subjects'

#Modules Detailview view.
class ModulesRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Modules.objects.all()
    serializer_class = ModuleSerializer
    lookup_field = "modules_id"

from exam.serializer import ExamSerializer
from exam.models import Exam
#list and write exams
class ExamsNestedView(ListCreateAPIView):
    permisson_classes = [IsAdminUser]
    serializer_class = ExamSerializer
    lookup_field = "modules_id"

    def get_queryset(self):
        modules_id = self.kwargs["modules_id"] #extract 'slug_modules'
        modules = Modules.objects.get(modules_id = modules_id)   #extract modules based on that 'slug_modules'
        return modules.exams.all()  #extract all exams based on that 'slug_modules'

#Exams inside Modules Detailview
class ExamsNestedRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    lookup_field = "exam_unique_id"

#list and write videos
class videosNestedView(ListCreateAPIView):
    permisson_classes = [IsAdminUser]
    serializer_class = VideoNestedSerializer
    lookup_field = "modules_id"

    def get_queryset(self):
        modules_id = self.kwargs["modules_id"] #extract 'slug_modules'
        modules = Modules.objects.get(modules_id = modules_id)  #extract modules based on that 'slug_modules'
        return modules.videos.all()   #extract all videos based on that 'slug_modules'

#Videos inside Modules Detailview
class VideosNestedRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = videosNested.objects.all()
    serializer_class = VideoNestedSerializer
    lookup_field = "video_unique_id"

#list and write notes
class NotesNestedView(ListCreateAPIView):
    permisson_classes = [IsAdminUser]
    serializer_class = NotesNestedSerializer
    lookup_field = "modules_id"

    def get_queryset(self):
        modules_id = self.kwargs["modules_id"]  #extract 'slug_modules'
        modules = Modules.objects.get(modules_id = modules_id)  #extract modules based on that 'slug_modules'
        return modules.notes.all()  #extract all notes based on that 'slug_modules'

#Videos inside Modules Detailview
class NotesNestedRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = NotesNested.objects.all()
    serializer_class = NotesNestedSerializer
    lookup_field = "notes_id"

from .models import SliderImage
from .serializers import SliderImageSerializer

class SliderImageAdd(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SliderImageSerializer
    queryset = SliderImage.objects.all()
    
    
class SliderImageRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SliderImageSerializer
    queryset = SliderImage.objects.all()
    lookup_field = "images_id"

from .models import PopularCourses
from .serializers import PopularCourseSerializer

class PopularCoursesAdd(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = PopularCourses.objects.all()
    serializer_class = PopularCourseSerializer

class PopularCourseRetrieveUpdateDestroyview(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PopularCourseSerializer
    queryset = PopularCourses.objects.all()
    lookup_field = "popular_course_id"
    
#view to assign a exam to a user.
class AssignExam(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        #get exam id and username of the user.
        username = request.data.get('username')
        exam = request.data.get('exam_unique_id')
        
        #get associated user and exam
        try:
            exam = Exam.objects.get(exam_unique_id = exam)
            user = RegularUserModel.objects.get(username = username)
        except RegularUserModel.DoesNotExist:
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        except Exam.DoesNotExist:
            return Response("Exam not found", status=status.HTTP_404_NOT_FOUND)

        duration = int(request.data.get('duration')) #duration in days        
        
        date_of_purchase = timezone.now()
        expiration_date = date_of_purchase + timezone.timedelta(days=duration)

        user_profile, created = UserProfile.objects.get_or_create(user = user)
        user_profile.purchased_exams.add(exam)

        purchased_date = PurchasedDate.objects.create(user_profile=user_profile,
                                                      exam = exam, 
                                                        date_of_purchase=timezone.now(),
                                                        expiration_date = expiration_date)
        purchased_date.save()

        return Response("Exam purchased successfully", status=status.HTTP_200_OK)

#view to assign a course to a user.
class AssignCourses(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        #get coures_id and username of the user.
        username = request.data.get('username')
        course_id = request.data.get('course_unique_id')
        
        #get associated user and course.
        try:
            course = FieldOfStudy.objects.get(course_unique_id = course_id)
            
            user = RegularUserModel.objects.get(username = username)
        
        except RegularUserModel.DoesNotExist:
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        except FieldOfStudy.DoesNotExist:
            return Response("Course not found", status=status.HTTP_404_NOT_FOUND)
   
        duration = int(request.data.get('duration')) #duration in days
        date_of_purchase = timezone.now()
        expiration_date = date_of_purchase + timezone.timedelta(days=duration)

        user_profile, created = UserProfile.objects.get_or_create(user = user)
        user_profile.purchased_courses.add(course)

        purchased_date = PurchasedDate.objects.create(user_profile=user_profile, 
                                                      course = course,
                                                        date_of_purchase=timezone.now(),
                                                        expiration_date = expiration_date)

        return Response("Course purchased successfully", status=status.HTTP_200_OK)

        
class ViewAllUsers(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = RegularUserSerializer
    queryset = RegularUserModel.objects.all()

class ViewUserDetial(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = RegularUserSerializer
    queryset = RegularUserModel
    lookup_field = 'username'
