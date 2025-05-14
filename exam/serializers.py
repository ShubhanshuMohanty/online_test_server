from .models import McqQuestion
from rest_framework import serializers

class McqQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = McqQuestion
        fields = ['id', 'batch', 'exam_name', 'question', 'option1', 'option2', 'option3', 'option4', 'answer', 'created_at']

