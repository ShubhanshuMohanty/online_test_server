from django.contrib import admin
from .models import McqQuestion
# Register your models here.
@admin.register(McqQuestion)
class AdminMcqQuestion(admin.ModelAdmin):
    list_display = ('batch','exam_name','question', 'option1', 'option2', 'option3', 'option4', 'answer')
    search_fields = ('batch','exam_name',)
    list_filter = ('batch','exam_name',)
    ordering = ('-id',)
