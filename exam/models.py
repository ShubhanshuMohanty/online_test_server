from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class McqQuestion(models.Model):
    batch=models.CharField(max_length=100)
    exam_name=models.CharField(max_length=100)
    question=models.TextField()
    option1=models.CharField(max_length=1000)
    option2=models.CharField(max_length=1000)
    option3=models.CharField(max_length=1000,null=True, blank=True)
    option4=models.CharField(max_length=1000,null=True, blank=True)
    ANSWER_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
    ]
    answer = models.CharField(max_length=10, choices=ANSWER_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    def get_correct_answer_text(self):
        return getattr(self, self.answer)

