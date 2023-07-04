from django.urls import path
from .views import (CoursesList, CoursesRetrieveView,
                    SubjectsList, SubjectsRetrieveView,
                    ModulesList, ModulesRetrieveView,
                     UserProfileView,BuyCourse)
urlpatterns = [
    path('courses/', CoursesList.as_view(), name='courses'),
    path('courses/<str:slug_studyfield>/', CoursesRetrieveView.as_view(), name='coursesretrieve'),
    path('courses/<str:slug_studyfield>/subjects/', SubjectsList.as_view(), name='subjects'),
    path('courses/<str:slug_studyfield>/subjects/<str:slug_subjects>/', SubjectsRetrieveView.as_view(), name='subjectsretrieve'),
    path('courses/<str:slug_studyfield>/subjects/<str:slug_subjects>/modules/', ModulesList.as_view(), name='modules'),
    path('courses/<str:slug_studyfield>/subjects/<str:slug_subjects>/modules/<str:slug_modules>/', ModulesRetrieveView.as_view(), name='modulesretrieve'),
    path('courses/<str:slug_studyfield>/buycourse/', BuyCourse.as_view(), name='buy_course'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]
