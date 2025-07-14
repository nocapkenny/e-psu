from django.db import models

from userapp.models import TeacherProfile, StudentProfile

class SchoolClass(models.Model):
    
    name = models.CharField(max_length = 15) 
    homeroom_teacher = models.ForeignKey(TeacherProfile, on_delete = models.CASCADE, related_name = 'homeroom_teacher')
    date = models.PositiveIntegerField()
    current = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.name} класс {self.date} года'
    
class SchoolLesson(models.Model):
    
    name = models.CharField(max_length = 50)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    

class TeacherClassLesson(models.Model):
    
    teacher = models.ForeignKey(TeacherProfile, on_delete = models.CASCADE)
    lesson = models.ForeignKey(SchoolLesson, on_delete = models.CASCADE)
    classes = models.ForeignKey(SchoolClass, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'{self.teacher.user.get_full_name} ведет {self.lesson.name} у {self.classes.name} класса'
    
class StudentClass(models.Model):
    
    student = models.ForeignKey(StudentProfile, on_delete = models.CASCADE)
    class_num = models.ForeignKey(SchoolClass, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'{self.student.user.get_full_name()} {self.class_num.name} класс {self.class_num.date} года'
     