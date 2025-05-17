from django.contrib import admin
from .models import Profile
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'first_name', 'middle_name', 'last_name', 'batch', 'phone_number', 'course_name')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('batch',)
    ordering = ('username',)