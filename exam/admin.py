from django.contrib import admin
from .models import McqQuestion,Batch,Course,StudentExamRecord,Test
# Register your models here.
@admin.register(McqQuestion)
class AdminMcqQuestion(admin.ModelAdmin):
    list_display = ('batch','exam_name','question', 'option1', 'option2', 'option3', 'option4', 'answer')
    search_fields = ('batch','exam_name',)
    list_filter = ('batch','exam_name',)
    ordering = ('-id',)

@admin.register(Batch)
class AdminBatch(admin.ModelAdmin):
    list_display = ('batch_name',)
    search_fields = ('batch_name',)
    ordering = ('-id',)

@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('course_name',)
    search_fields = ('course_name',)
    ordering = ('-id',)

@admin.register(StudentExamRecord)
class AdminStudentExamRecord(admin.ModelAdmin):
    list_display = ('student', 'exam', 'completed_at', 'score')

@admin.register(Test)
class AdminTest(admin.ModelAdmin):
    list_display = ('name', 'batch', 'duration_minutes', 'number_of_questions', 'created_at')
    
    