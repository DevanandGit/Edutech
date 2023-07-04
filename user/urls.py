from django.urls import path
from .views import RegularUserRegisterationView,RegularUserLoginView, RegularUserLogoutView, AdminLoginView, AdminLogoutView,AdminRegistrationView
from .views import (TeacherRetrieveUpdateDestroyView,TeacherListCreateView,FieldOfStudyListCreateView, FieldOfStudyRetrieveUpdateDestroyView, SubjectsListCreateView,
                    SubjectsRetrieveUpdateDestroyView, ModulesListCreateView,ModulesRetrieveUpdateDestroyView, 
                    AccessTypeListCreateView,AccessTypeRetrieveUpdateDestroyView,ExamsNestedView, ExamsNestedRetrieveUpdateDestroyView,
                    videosNestedView, VideosNestedRetrieveUpdateDestroyView, NotesNestedView, NotesNestedRetrieveUpdateDestroyView)

urlpatterns = [
    #urls for regular user.
    path('userRegistration/', RegularUserRegisterationView.as_view(), name='userregistration'),
    path('login/', RegularUserLoginView.as_view(), name='userlogin'),
    path('logout/', RegularUserLogoutView.as_view(), name='userlogout'),
    
    #urls for admin.
    path('adminregistration/', AdminRegistrationView.as_view(), name='adminregistration'),
    path('adminlogin/', AdminLoginView.as_view(), name='adminlogin'),
    path('adminlogout/', AdminLogoutView.as_view(), name='adminlogout'),

    #urls for courses.This urls is only for admin to add, update or view courses.
    path('teacheradd/', TeacherListCreateView.as_view(), name='teacheradd'),
    path('teacheradd/<int:pk>/', TeacherRetrieveUpdateDestroyView.as_view(), name='teacheradd'),
    path("access-type-add/", AccessTypeListCreateView.as_view(), name='accesstypeadd'),
    path("access-type-add/<int:pk>", AccessTypeRetrieveUpdateDestroyView.as_view(), name='accesstypeadd'),
    path('fieldofstudy/', FieldOfStudyListCreateView.as_view(), name='fieldofstudy-list'),
    path('fieldofstudy/<str:slug_studyfield>/', FieldOfStudyRetrieveUpdateDestroyView.as_view(), name='fieldofstudy-detail'),
    path('fieldofstudy/<str:slug_studyfield>/subjects/', SubjectsListCreateView.as_view(), name='subjects-list'),
    path('fieldofstudy/<str:slug_studyfield>/subjects/<str:slug_subjects>/', SubjectsRetrieveUpdateDestroyView.as_view(), name='subjects-detail'),
    path('fieldofstudy/<str:slug_studyfield>/subjects/<str:slug_subjects>/modules/', ModulesListCreateView.as_view(), name='modules-list'),
    path('fieldofstudy/<str:slug_studyfield>/subjects/<str:slug_subjects>/modules/<str:slug_modules>/', ModulesRetrieveUpdateDestroyView.as_view(), name='modules-detail'),
    path('fieldofstudy/<str:slug_studyfield>/subjects/<str:slug_subjects>/modules/<str:slug_modules>/notes/', NotesNestedView.as_view(), name='notes-list'),
    path('fieldofstudy/<str:slug_studyfield>/subjects/<str:slug_subjects>/modules/<str:slug_modules>/notes/<str:slug_notes>', NotesNestedRetrieveUpdateDestroyView.as_view(), name='notes-detail'),
    path('fieldofstudy/<str:slug_studyfield>/subjects/<str:slug_subjects>/modules/<str:slug_modules>/exams/', ExamsNestedView.as_view(), name='exams-list'),
    path('fieldofstudy/<str:slug_studyfield>/subjects/<str:slug_subjects>/modules/<str:slug_modules>/exams/<str:slug_exams>', ExamsNestedRetrieveUpdateDestroyView.as_view(), name='exams-detail'),
    path('fieldofstudy/<str:slug_studyfield>/subjects/<str:slug_subjects>/modules/<str:slug_modules>/videos/', videosNestedView.as_view(), name='videos-list'),
    path('fieldofstudy/<str:slug_studyfield>/subjects/<str:slug_subjects>/modules/<str:slug_modules>/videos/<str:slug_videos>', VideosNestedRetrieveUpdateDestroyView.as_view(), name='videos-detail'),
]

