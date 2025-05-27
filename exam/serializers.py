from .models import McqQuestion,Course,Batch, StudentExamRecord
from rest_framework import serializers

class McqQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = McqQuestion
        fields = ['id', 'batch', 'test_name','exam_name', 'question', 'option1', 'option2', 'option3', 'option4', 'answer', 'created_at']

class CourseSerializer(serializers.ModelSerializer):
    class Meta :
        model= Course
        fields = ['id', 'course_name']

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['id', 'batch_name']

class StudentExamRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentExamRecord
        fields = ['id', 'student', 'exam', 'started_at', 'completed_at', 'score']
        read_only_fields = ['started_at', 'completed_at', 'score']