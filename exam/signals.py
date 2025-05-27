# signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import McqQuestion, Test,StudentExamRecord
from user_auth.models import Profile
from django.db import transaction

@receiver(post_save, sender=McqQuestion)
def update_question_count_on_save(sender, instance, **kwargs):
    test = instance.test_name
    test.number_of_questions = test.questions.count()
    test.save()

@receiver(post_delete, sender=McqQuestion)
def update_question_count_on_delete(sender, instance, **kwargs):
    test = instance.test_name
    test.number_of_questions = test.questions.count()
    test.save()


# 1. Jab naya Test create ho
@receiver(post_save, sender=Test)
def create_exam_records_for_existing_students(sender, instance, created, **kwargs):
    print(f"Test created: {instance.name}, Batch: {instance.batch.batch_name}")
    if created:
        test_batch = instance.batch
        question_count = instance.questions.count()

        # Sabhi students jinka batch is test ke batch ke equal hai
        matching_profiles = Profile.objects.filter(batch=test_batch)
        print(f"Creating exam records for {matching_profiles.count()} students in batch {test_batch.batch_name} for test {instance.name}")
        with transaction.atomic():
            for profile in matching_profiles:
                StudentExamRecord.objects.create(
                    student=profile.user,
                    exam=instance,
                    marks=question_count,
                    # score=question_count
                )

# 2. Jab naya student Profile create ho
@receiver(post_save, sender=Profile)
def create_exam_records_for_new_student(sender, instance, created, **kwargs):
    print(f"Profile created for user: {instance.user.username}, batch: {instance.batch.batch_name}")
    if created:
        student_user = instance.user
        student_batch = instance.batch

        # Us batch ke sare tests
        matching_tests = Test.objects.filter(batch=student_batch)

        with transaction.atomic():
            for test in matching_tests:
                # Agar record already exist nahi karta
                if not StudentExamRecord.objects.filter(student=student_user, exam=test).exists():
                    print("test=", test.name, "student=", student_user.username)
                    StudentExamRecord.objects.create(
                        student=student_user,
                        exam=test,
                        marks=test.questions.count(),
                        # score=test.questions.count()
                    )

@receiver(post_save, sender=McqQuestion)
def update_marks_on_new_question(sender, instance, created, **kwargs):
    if created:
        test = instance.test_name
        question_count = test.questions.count()
        test_batch = test.batch

        # Sare student records jinka exam yeh test hai aur student batch same hai
        records = StudentExamRecord.objects.filter(exam=test, student__profile__batch=test_batch)

        with transaction.atomic():
            for record in records:
                record.marks = question_count
                record.score = question_count  # Optional: depends on your logic
                record.save()