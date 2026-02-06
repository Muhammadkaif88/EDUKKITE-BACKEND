from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_locked', 'created_at')
    list_filter = ('is_locked', 'created_at')
    search_fields = ('title', 'subtitle')
