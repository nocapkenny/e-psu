from rest_framework import serializers

from schooltable.models import SchoolClass, SchoolLesson, StudentClass, TeacherClassLesson
from userapp.serializers import CustomUserSerlializer, TeacherProfileSerializer, TeacherProfileMiniSerializer
from userapp.models import StudentProfile


class SchoolClassSerializer(serializers.ModelSerializer):
    
    homeroom_teacher = CustomUserSerlializer()
    
    class Meta:
         model = SchoolClass
         fields = ('id', 'name', 'homeroom_teacher', 'date')
         
         

        
        
#---Для учителя классы + предмет класса, ученики по классу

class StudentProfileUserSerializer(serializers.ModelSerializer):
    mail = serializers.EmailField(source = 'user.mail')
    first_name = serializers.CharField(source = 'user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    middle_name = serializers.CharField(source = 'user.middle_name')
    class Meta:
        model = StudentProfile
        fields = ('mail', 'first_name', 'last_name', 'middle_name')



class StudentClassSerializer(serializers.ModelSerializer):
        
    student = StudentProfileUserSerializer(read_only=True) 
    
    class Meta:
        model = StudentClass
        fields = ('id', 'student')
        

class SchoolLessonMiniSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SchoolLesson
        fields = ('id', 'name')
    
        
class SchoolClassMiniSerializer(serializers.ModelSerializer):
    
    class Meta:
         model = SchoolClass
         fields = ('id', 'name', 'date')
         
     
class TeacherClassLessonSerializer(serializers.ModelSerializer):
    
    classes = SchoolClassMiniSerializer()
    lesson = SchoolLessonMiniSerializer()
    
    class Meta:
        model = TeacherClassLesson
        fields = ('id', 'classes', 'lesson')
        
        
class SchoolClassStudentsSerializer(serializers.ModelSerializer):
    
    homeroom_teacher = TeacherProfileMiniSerializer()
    students = serializers.SerializerMethodField()

    class Meta:
        model = SchoolClass
        fields = ('id', 'name', 'date', 'homeroom_teacher', 'students')

    def get_students(self, obj):
        students = StudentClass.objects.filter(class_num=obj).select_related('student__user')
        return StudentClassSerializer(students, many=True).data

#---

class SchoolLessonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SchoolLesson
        fields = ('id', 'name', 'description')