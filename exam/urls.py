from django.urls import path
from .views import (QuestionTypeListCreateView, QuestionTypeRetrieveUpdateDestroyView, 
                    MultipleChoiceListCreateView, MultipleChoiceRetrieveUpdateDestroyView,
                    MultiSelectListCreateView, MultiSelectRetrieveUpdateDestroyView,
                    OptionsListCreateView, OptionsRetrieveUpdateDestroyView,
                    NumericalsListCreateView, NumericalsRetrieveUpdateDestroyView,
                    ExamListCreateView, ExamRetrieveUpdateDestroyView)

urlpatterns = [

    #this urls is for admin to add,update and view questions.
    path('question-type/', QuestionTypeListCreateView.as_view(), name='exam'),
    path('question-type/<str:slug_question_type>/', QuestionTypeRetrieveUpdateDestroyView.as_view(), name='exam'),
    path('addexam/', ExamListCreateView.as_view(), name='exam'),
    path('addexam/<str:slug_exam>/', ExamRetrieveUpdateDestroyView.as_view(), name='exam'),
    path('addexam/<str:slug_exam>/multiplechoice/', MultipleChoiceListCreateView.as_view(), name='multiplechoice-list'),
    path('addexam/<str:slug_exam>/multiplechoice/<str:slug_multiplechoice>/', MultipleChoiceRetrieveUpdateDestroyView.as_view(), name='multiplechoice-detail'),
    path('addexam/<str:slug_exam>/multiselect/', MultiSelectListCreateView.as_view(), name='multiselect-list'),
    path('addexam/<str:slug_exam>/multiselect/<str:slug_multiselect>/', MultiSelectRetrieveUpdateDestroyView.as_view(), name='multiselect-detail'),
    path('addexam/<str:slug_exam>/multiselect/<str:slug_multiselect>/options/', OptionsListCreateView.as_view(), name='multiselect-options-list'),
    path('addexam/<str:slug_exam>/multiselect/<str:slug_multiselect>/options/<str:slug_options/', OptionsRetrieveUpdateDestroyView.as_view(), name='multiselect-options-detail'),
    path('addexam/<str:slug_exam>/numericals/', NumericalsListCreateView.as_view(), name='numericals-list'),
    path('addexam/<str:slug_exam>/numericals/<str:slug_numericals>/', NumericalsRetrieveUpdateDestroyView.as_view(), name='numericals-detail'),
]
