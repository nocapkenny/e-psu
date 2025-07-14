from rest_framework import serializers

from userapp.models import CustomUser, StudentProfile, TeacherProfile


class CustomUserSerlializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id', 'mail', 'last_name', 'first_name', 'middle_name', 'photo')
        
class StudentProfileSerializer(serializers.ModelSerializer):
    
    user = CustomUserSerlializer()
    
    class Meta:
        model = StudentProfile
        fields = ('id', 'user', 'parents_contacts', 'enrollment_date')
        
class TeacherProfileSerializer(serializers.ModelSerializer):
    
    user = CustomUserSerlializer()
    
    class Meta: 
        model = TeacherProfile
        fields = ('id', 'user', 'work_experience', 'awards')
        
class TeacherProfileMiniSerializer(serializers.ModelSerializer):
    
    user = CustomUserSerlializer()
    
    class Meta:
        model = TeacherProfile
        fields = ('id', 'user')