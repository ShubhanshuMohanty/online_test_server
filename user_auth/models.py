from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from exam.models import Course, Batch
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='students')
    phone_number = models.CharField(max_length=15, unique=True)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.user.username
