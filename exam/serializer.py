from rest_framework import serializers
from .models import (Exam, MultipleChoice,Numericals, QuestionType,)
from .models import MultiSelect, Options
#Validate QuestionType-Multiplechoice, multiselect, numericals
class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ["question_type", 'slug_question_type']

#Validate Options of Multiselect
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['option_id','question','option_no', 'options_text', 'options_image','is_answer', 'slug_options']

#Validate Multiplechoice questions data
class MultipleChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoice
        fields = ['mcq_id','question_type','exam_name', 'question_no','question', 'question_image','option1_text','option2_text','option3_text','option4_text','option1_image','option2_image','option3_image','option4_image','positive_marks','negetive_mark','choose','answer','solution_text','solution_image','slug_multiplechoice']

#Validate Multiselect questions data
class MultiSelectSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many = True, read_only = True)
    class Meta:
        model = MultiSelect
        fields = ['msq_id','question_no','question_type','exam_name','question','question_image','positive_marks','negetive_mark', 'options','solution_image','solution_text','slug_multiselect']

##Validate Numerical question data
class NumericalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numericals
        fields = ['nq_id','question_type','exam_name','question_no','question','question_image','ans_min_range','ans_max_range','answer','positive_marks','negetive_mark','solution_text','solution_image','slug_numericals']

#validates Exam data.
class ExamSerializer(serializers.ModelSerializer):
    multiplechoice = MultipleChoiceSerializer(many = True, read_only =True)
    multiselect = MultiSelectSerializer(many = True, read_only =True)
    numericals = NumericalSerializer(many=True, read_only=True)
    no_of_questions = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = ['exam_unique_id','module','access_type','exam_id','exam_name','instruction','duration_of_exam','total_marks','no_of_questions','created_date','updated_date','slug_exams','is_active', 'multiplechoice','multiselect','numericals']

    def get_no_of_questions(self, obj):
        return (obj.multiplechoice.count() + obj.multiselect.count() +obj.numericals.count())