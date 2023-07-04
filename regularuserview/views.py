from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from user.models import FieldOfStudy, Subjects, Modules,RegularUserModel
from user.serializers import FieldOfStudySerializer, SubjectSerializer, ModuleSerializer, RegularUserSerializer
from exam.models import Exam
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status

#course List
class CoursesList(ListAPIView):
    queryset = FieldOfStudy.objects.all()
    serializer_class = FieldOfStudySerializer

#Course DetailView
class CoursesRetrieveView(RetrieveAPIView):
    queryset = FieldOfStudy.objects.all()
    serializer_class = FieldOfStudySerializer
    lookup_field = 'slug_studyfield'

#subjects List view
class SubjectsList(ListAPIView):
    serializer_class = SubjectSerializer
    lookup_field = 'slug_studyfield'

    def get_queryset(self):
        slug_studyfield = self.kwargs['slug_studyfield']
        course = FieldOfStudy.objects.get(slug_studyfield = slug_studyfield)
        return course.subjects.all()

#subjects Detail view
class SubjectsRetrieveView(RetrieveAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = 'slug_subjects'

#Modules List view
class ModulesList(ListAPIView):
    serializer_class = ModuleSerializer
    lookup_field = 'slug_subjects'

    def get_queryset(self):
        slug_subjects = self.kwargs['slug_subjects']
        subjects = Subjects.objects.get(slug_subjects = slug_subjects)
        return subjects.modules.all()

#Modules Detail view
class ModulesRetrieveView(RetrieveAPIView):
    queryset = Modules.objects.all()
    serializer_class = ModuleSerializer
    lookup_field = 'slug_modules'
    
# Buy Course
class BuyCourse(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, slug_studyfield):
        try:
            course = FieldOfStudy.objects.get(slug_studyfield = slug_studyfield)
        except FieldOfStudy.DoesNotExist:
            return Response("Course not found", status=status.HTTP_404_NOT_FOUND)
        course = PurchasedCourses.objects.get(slug_purchasecustom = slug_studyfield)
        
        request.user.purhcased_course.add(course)

        return Response("Course purchased successfully", status=status.HTTP_200_OK)

#User Profile View.
class UserProfileView(RetrieveAPIView):
    serializer_class = RegularUserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


