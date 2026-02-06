from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'subtitle', 'thumbnail', 'is_locked', 'price', 'created_at', 'updated_at']
