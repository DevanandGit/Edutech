from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import (QuestionTypeSerializer,OptionSerializer,
                          MultipleChoiceSerializer,MultiSelectSerializer,
                            NumericalSerializer, ExamSerializer)
from .models import (QuestionType,Options,
                    MultipleChoice,MultiSelect,
                    Numericals, Exam)
from rest_framework.permissions import IsAdminUser

#listview for Question type list
class QuestionTypeListCreateView(ListCreateAPIView):
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer
    permission_classes = [IsAdminUser]

#Detail view of QuestionType
class QuestionTypeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer
    lookup_field = "slug_question_type"


#listview of Exams
class ExamListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
 

#Detail view of Exams
class ExamRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    lookup_field = "slug_exam"
    

#listview for Numericals questions
class NumericalsListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Numericals.objects.all()
    serializer_class = NumericalSerializer
    lookup_field = 'slug_exam'

    def get_queryset(self):
        slug_exam = self.kwargs['slug_exam']
        exam_name = Exam.objects.get(slug_exam = slug_exam)
        return exam_name.numericals.all()
    

#Detail view of Numericals Questions
class NumericalsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Numericals.objects.all()
    serializer_class = NumericalSerializer
    lookup_field = "slug_numericals"
    

#listview for Multipletype questions
class MultipleChoiceListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = MultipleChoice.objects.all()
    serializer_class = MultipleChoiceSerializer
    lookup_field = 'slug_exam'
    
    
    def get_queryset(self):
        slug_exam = self.kwargs['slug_exam']
        exam_name = Exam.objects.get(slug_exam = slug_exam)
        return exam_name.multiplechoice.all()

#Detail view of Multipletype questions
class MultipleChoiceRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = MultipleChoice.objects.all()
    serializer_class = MultipleChoiceSerializer
    lookup_field = "slug_multiplechoice"

#listview for Multiselect questions
class MultiSelectListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = MultiSelect.objects.all()
    serializer_class = MultiSelectSerializer
    lookup_field = 'slug_exam'
    
    def get_queryset(self):
        slug_exam = self.kwargs['slug_exam']
        exam_name = Exam.objects.get(slug_exam = slug_exam)
        return exam_name.multiselect.all()

#Detailview for Multiselect questions
class MultiSelectRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = MultiSelect.objects.all()
    serializer_class = MultiSelectSerializer
    lookup_field = "slug_multiselect"

#List view of options of multiselect questions.
class OptionsListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = OptionSerializer
    lookup_field = "slug_multiselect"

    def get_queryset(self):
        slug_multiselect = self.kwargs["slug_multiselect"]
        question_no = MultiSelect.objects.get(slug_multiselect = slug_multiselect)
        return question_no.options.all()
    
#DetailView of options of multiselect Questions
class OptionsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Options.objects.all()
    serializer_class = OptionSerializer
    lookup_field = "slug_options"