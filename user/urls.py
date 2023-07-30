from django.urls import path
from .views import RegularUserRegisterationView,RegularUserLoginView, RegularUserLogoutView, AdminLoginView, AdminLogoutView,AdminRegistrationView
from .views import (FieldOfStudyListCreateView, FieldOfStudyRetrieveUpdateDestroyView, SubjectsListCreateView,
                    SubjectsRetrieveUpdateDestroyView, ModulesListCreateView,ModulesRetrieveUpdateDestroyView, 
                    AccessTypeListCreateView,AccessTypeRetrieveUpdateDestroyView,ExamsNestedView, ExamsNestedRetrieveUpdateDestroyView,
                    videosNestedView, VideosNestedRetrieveUpdateDestroyView, NotesNestedView, NotesNestedRetrieveUpdateDestroyView, PopularCourseRetrieveUpdateDestroyview,
                    PopularCoursesAdd, SliderImageRetrieveUpdateDestroyView, SliderImageAdd)
from exam.views import (NumericalsListCreateView, NumericalsRetrieveUpdateDestroyView, MultipleChoiceListCreateView, MultipleChoiceRetrieveUpdateDestroyView,
                        MultiSelectListCreateView, MultiSelectRetrieveUpdateDestroyView, OptionsListCreateView, OptionsRetrieveUpdateDestroyView)
                        
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

    path("access-type-add/", AccessTypeListCreateView.as_view(), name='accesstypeadd'),
    path("access-type-add/<int:pk>", AccessTypeRetrieveUpdateDestroyView.as_view(), name='accesstypeadd'),
    path('fieldofstudy/', FieldOfStudyListCreateView.as_view(), name='fieldofstudy-list'),
    path('fieldofstudy/<int:course_unique_id>/', FieldOfStudyRetrieveUpdateDestroyView.as_view(), name='fieldofstudy-detail'),
    path('fieldofstudy/<int:course_unique_id>/subjects/', SubjectsListCreateView.as_view(), name='subjects-list'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/', SubjectsRetrieveUpdateDestroyView.as_view(), name='subjects-detail'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/', ModulesListCreateView.as_view(), name='modules-list'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/', ModulesRetrieveUpdateDestroyView.as_view(), name='modules-detail'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/notes/', NotesNestedView.as_view(), name='notes-list'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/notes/<int:notes_id>', NotesNestedRetrieveUpdateDestroyView.as_view(), name='notes-detail'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/videos/', videosNestedView.as_view(), name='videos-list'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/videos/<int:video_unique_id>', VideosNestedRetrieveUpdateDestroyView.as_view(), name='videos-detail'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/exams/', ExamsNestedView.as_view(), name='exams-list'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/exams/<int:exam_unique_id>', ExamsNestedRetrieveUpdateDestroyView.as_view(), name='exams-detail'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/exams/<int:exam_unique_id>/multiplechoice/', MultipleChoiceListCreateView.as_view(), name='exams-detail'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/exams/<int:exam_unique_id>/multiplechoice/<int:mcq_id>/', MultipleChoiceRetrieveUpdateDestroyView.as_view(), name='exams-detail'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/exams/<int:exam_unique_id>/multiselect/', MultiSelectListCreateView.as_view(), name='exams-detail'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/exams/<int:exam_unique_id>/multiselect/<int:msq_id>/', MultiSelectRetrieveUpdateDestroyView.as_view(), name='exams-detail'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/exams/<int:exam_unique_id>/multiselect/<int:msq_id>/options/', OptionsListCreateView.as_view(), name='exams-detail'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/exams/<int:exam_unique_id>/multiselect/<int:msq_id>/options/<int:option_id>/', OptionsRetrieveUpdateDestroyView.as_view(), name='exams-detail'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/exams/<int:exam_unique_id>/numericals/', NumericalsListCreateView.as_view(), name='exams-detail'),
    path('fieldofstudy/<int:course_unique_id>/subjects/<int:subject_id>/modules/<int:modules_id>/exams/<int:exam_unique_id>/numericals/<int:nq_id>/', NumericalsRetrieveUpdateDestroyView.as_view(), name='exams-detail'),

    path('sliderimageadd/', SliderImageAdd.as_view(), name='sliderimageadd'),
    path('sliderimageadd/<int:images_id>', SliderImageRetrieveUpdateDestroyView.as_view(), name='sliderimageadd'),
    path('popularcourseadd/', PopularCoursesAdd.as_view(), name='popularcourseadd'),
    path('popularcourseadd/<int:popular_course_id>', PopularCourseRetrieveUpdateDestroyview.as_view(), name='popularcourseadd'),

]

