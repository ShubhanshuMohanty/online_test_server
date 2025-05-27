from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class McqQuestion(models.Model):
    test_name = models.ForeignKey('Test', on_delete=models.CASCADE, related_name='questions')
    batch=models.ForeignKey('Batch', on_delete=models.CASCADE)
    exam_name=models.ForeignKey('Course', on_delete=models.CASCADE)
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
    def __str__(self):
        return f"{self.test_name} - {self.exam_name}"

class Batch(models.Model):
    batch_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.batch_name

from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.course_name

class StudentExamRecord(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey('Test', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    marks= models.FloatField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('student', 'exam')

class Test(models.Model):
    name = models.CharField(max_length=100)
    batch = models.ForeignKey('Batch', on_delete=models.CASCADE)
    duration_minutes = models.PositiveIntegerField(default=30)
    number_of_questions = models.PositiveIntegerField(default=0)  # ← Add this field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

