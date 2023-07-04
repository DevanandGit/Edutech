from rest_framework import serializers
from .models import (Exam, MultipleChoice,Numericals, QuestionType,MultiSelect, Options)

#Validate QuestionType-Multiplechoice, multiselect, numericals
class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ["question_type", 'slug_question_type']

#Validate Options of Multiselect
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['id','question','option_no', 'options', 'is_answer', 'slug_options']

#Validate Multiplechoice questions data
class MultipleChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoice
        fields = ['question_type','exam_name', 'question_no','question', 'question_image','option1','option2','option3','option4','marks','choose','answer','slug_multiplechoice']

#Validate Multiselect questions data
class MultiSelectSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many = True, read_only = True)
    class Meta:
        model = MultiSelect
        fields = ['id','question_no','question_type','exam_name','question','question_image','marks', 'options','slug_multiselect']

##Validate Numerical question data
class NumericalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numericals
        fields = ['question_type','exam_name','question_no','question','question_image','ans_min_range','ans_max_range','answer','slug_numericals']

#validates Exam data.
class ExamSerializer(serializers.ModelSerializer):
    multiplechoice = MultipleChoiceSerializer(many = True, read_only =True)
    multiselect = MultiSelectSerializer(many = True, read_only =True)
    numericals = NumericalSerializer(many=True, read_only=True)
    no_of_questions = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = ['id','access_type','exam_name','exam_id','instruction','duration_of_exam','total_marks','no_of_questions','created_date','updated_date','slug_exam','is_active', 'multiplechoice','multiselect','numericals']

    def get_no_of_questions(self, obj):
        return (obj.multiplechoice.count() + obj.multiselect.count() +obj.numericals.count())