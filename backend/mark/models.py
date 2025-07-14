from django.db import models

from userapp.models import StudentProfile, TeacherProfile
from schooltable.models import SchoolLesson

class Mark(models.Model):
    
    MARK_CHOICES = [
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
    ]
    QUARTER_CHOICES = [
        ('1', '1 четверть'),
        ('2', '2 четверть'),
        ('3', '3 четверть'),
        ('4', '4 четверть'),
    ]
    TYPE_CHOICES = [
        ('homework', 'Домашнее задание'),
        ('test', 'Тест'),
        ('exam', 'Экзамен'),
        ('verbal_answer', 'Устный ответ'),
        ('project', 'Проект'),
    ]
    
    student = models.ForeignKey(StudentProfile, on_delete = models.PROTECT)
    teacher = models.ForeignKey(TeacherProfile, on_delete = models.PROTECT)
    lesson = models.ForeignKey(SchoolLesson, on_delete = models.PROTECT)
    date = models.DateField(auto_now_add = True)
    quarter = models.CharField(max_length = 1, choices = QUARTER_CHOICES)
    mark_type = models.CharField(max_length = 30, choices = TYPE_CHOICES)
    value = models.CharField(max_length = 1, choices = MARK_CHOICES)
    
    def __str__(self):
        return f'{self.student.user.get_full_name()} - {self.value} по {self.lesson.name}'