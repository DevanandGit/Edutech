from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import (QuestionTypeSerializer,
                          MultipleChoiceSerializer,
                            NumericalSerializer, ExamSerializer)

from .models import (QuestionType,
                    MultipleChoice,
                    Numericals, Exam)
from .serializer import MultiSelectSerializer,OptionSerializer
from .models import Options,MultiSelect
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
    lookup_field = "exam_unique_id"
    

#listview for Numericals questions
class NumericalsListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Numericals.objects.all()
    serializer_class = NumericalSerializer
    lookup_field = 'exam_unique_id'

    def get_queryset(self):
        exam_unique_id = self.kwargs['exam_unique_id']
        exam_name = Exam.objects.get(exam_unique_id = exam_unique_id)
        return exam_name.numericals.all()
    

#Detail view of Numericals Questions
class NumericalsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Numericals.objects.all()
    serializer_class = NumericalSerializer
    lookup_field = "nq_id"
    

#listview for Multipletype questions
class MultipleChoiceListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = MultipleChoice.objects.all()
    serializer_class = MultipleChoiceSerializer
    lookup_field = 'exam_unique_id'
    
    
    def get_queryset(self):
        exam_unique_id = self.kwargs['exam_unique_id']
        exam_name = Exam.objects.get(exam_unique_id = exam_unique_id)
        return exam_name.multiplechoice.all()

#Detail view of Multipletype questions
class MultipleChoiceRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = MultipleChoice.objects.all()
    serializer_class = MultipleChoiceSerializer
    lookup_field = "mcq_id"

#listview for Multiselect questions
class MultiSelectListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = MultiSelect.objects.all()
    serializer_class = MultiSelectSerializer
    lookup_field = 'exam_unique_id'
    
    def get_queryset(self):
        exam_unique_id = self.kwargs['exam_unique_id']
        exam_name = Exam.objects.get(exam_unique_id = exam_unique_id)
        return exam_name.multiselect.all()

#Detailview for Multiselect questions
class MultiSelectRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = MultiSelect.objects.all()
    serializer_class = MultiSelectSerializer
    lookup_field = "msq_id"

#List view of options of multiselect questions.
class OptionsListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = OptionSerializer
    lookup_field = "msq_id"

    def get_queryset(self):
        msq_id = self.kwargs["msq_id"]
        question_no = MultiSelect.objects.get(msq_id = msq_id)
        return question_no.options.all()

#DetailView of options of multiselect Questions
class OptionsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Options.objects.all()
    serializer_class = OptionSerializer
    lookup_field = "option_id"