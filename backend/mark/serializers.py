from rest_framework import serializers

from mark.models import Mark


class MarkSerializer(serializers.ModelSerializer):
    
    lesson = serializers.CharField(source = 'lesson.name')
    
    class Meta:
        model = Mark
        fields = ['id', 'lesson', 'date', 'quarter', 'mark_type', 'value']
        
class MarkPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mark
        fields = '__all__'

class MarkLessonSerializer(serializers.Serializer):
    
    lesson = serializers.CharField()
    mark = MarkSerializer(many = True)
    
class PostMarkSerializer(serializers.ModelSerializer):
    
    student_last_name = serializers.CharField(source = 'student.user.last_name')
    student_first_name = serializers.CharField(source = 'student.user.first_name')
    lesson = serializers.CharField(source = 'lesson.name')
    
    class Meta:
        model = Mark
        fields = ['id', 'student_last_name', 'student_first_name', 'lesson', 'date', 'quarter', 'mark_type', 'value']
        