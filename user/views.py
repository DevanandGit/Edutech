from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.utils import timezone
from .models import (Teachers, Access_type,
                    FieldOfStudy, Subjects, Modules,
                    ExamsNested, videosNested, NotesNested)
from .serializers import (RegularUserSerializer,RegularUserLoginSerializer,
                        AdminLoginSerializer, AdminRegistrationSerializer,
                        TeachersSerializer, Access_type_serializer,FieldOfStudySerializer,
                        ModuleSerializer,SubjectSerializer,ExamNestedSerializer,
                        VideoNestedSerializer, NotesNestedSerializer)

from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

#Regular user registration view.
class RegularUserRegisterationView(CreateAPIView):
    serializer_class = RegularUserSerializer

#Regular User login view.
class RegularUserLoginView(APIView):
    serializer_class = RegularUserLoginSerializer

    def post(self, request):
        serializer = RegularUserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, username=serializer.data['username'], password=serializer.data['password'])
        
        if user is not None:
            # Invalidate all sessions except for the current one
            active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
            for session in active_sessions:
                session_data = session.get_decoded()
                if str(user.pk) == session_data.get('_auth_user_id'):
                    Token.objects.filter(user=request.user).delete()
                    session.delete()
            
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
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

#Create Teachers view.
class TeacherListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer

#Teacher Detailview.
class TeacherRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer


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
    lookup_field = "slug_studyfield"

#Subjects overview view.
class SubjectsListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SubjectSerializer
    lookup_field = "slug_studyfield"

    def get_queryset(self):
        slug_studyfield = self.kwargs['slug_studyfield']  #extract all 'slug_studyfield'
        field_of_study = FieldOfStudy.objects.get(slug_studyfield=slug_studyfield) #extract FieldOfStudy objects based on that 'slug_studyfield'
        return field_of_study.subjects.all() #extract all subjects associated with that 'study_slugfield'

#Subjects Detailview View.
class SubjectsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = "slug_subjects"

#Modules OverView View.
class ModulesListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ModuleSerializer
    lookup_field = "slug_subjects"

    def get_queryset(self):
        slug_subjects = self.kwargs["slug_subjects"]  #extract all 'slug_subjects'
        subjects = Subjects.objects.get(slug_subjects = slug_subjects)  #extract all subjects based on that 'slug_subjects'
        return subjects.modules.all()  #extract all modules based on that 'study_subjects'

#Modules Detailview view.
class ModulesRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Modules.objects.all()
    serializer_class = ModuleSerializer
    lookup_field = "slug_modules"

#list and write exams
class ExamsNestedView(ListCreateAPIView):
    permisson_classes = [IsAdminUser]
    serializer_class = ExamNestedSerializer
    lookup_field = "slug_modules"

    def get_queryset(self):
        slug_modules = self.kwargs["slug_modules"] #extract 'slug_modules'
        modules = Modules.objects.get(slug_modules = slug_modules)   #extract modules based on that 'slug_modules'
        return modules.exams.all()  #extract all exams based on that 'slug_modules'

#Exams inside Modules Detailview
class ExamsNestedRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = ExamsNested.objects.all()
    serializer_class = ExamNestedSerializer
    lookup_field = "slug_exams"

#list and write videos
class videosNestedView(ListCreateAPIView):
    permisson_classes = [IsAdminUser]
    serializer_class = VideoNestedSerializer
    lookup_field = "slug_modules"

    def get_queryset(self):
        slug_modules = self.kwargs["slug_modules"] #extract 'slug_modules'
        modules = Modules.objects.get(slug_modules = slug_modules)  #extract modules based on that 'slug_modules'
        return modules.videos.all()   #extract all videos based on that 'slug_modules'

#Videos inside Modules Detailview
class VideosNestedRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = videosNested.objects.all()
    serializer_class = VideoNestedSerializer
    lookup_field = "slug_videos"

#list and write notes
class NotesNestedView(ListCreateAPIView):
    permisson_classes = [IsAdminUser]
    serializer_class = NotesNestedSerializer
    lookup_field = "slug_modules"

    def get_queryset(self):
        slug_modules = self.kwargs["slug_modules"]  #extract 'slug_modules'
        modules = Modules.objects.get(slug_modules = slug_modules)  #extract modules based on that 'slug_modules'
        return modules.notes.all()  #extract all notes based on that 'slug_modules'

#Videos inside Modules Detailview
class NotesNestedRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = NotesNested.objects.all()
    serializer_class = NotesNestedSerializer
    lookup_field = "slug_notes"