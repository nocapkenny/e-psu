from collections import defaultdict

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from schooltable.models import StudentClass, SchoolLesson, TeacherClassLesson, SchoolClass
from userapp.models import StudentProfile, TeacherProfile
from mark.models import Mark

from schooltable.serializers import SchoolLessonSerializer, TeacherClassLessonSerializer
from mark.serializers import MarkSerializer, MarkLessonSerializer


def currentQuarter():
    from datetime import datetime
    month = datetime.now().month
    if month in [1, 2, 3, 4]:
        return '1'
    elif month in [5, 6, 7, 8]:
        return '2'
    elif month in [9, 10, 11]:
        return '3'
    else:
        return '4'  

class MarkChoisesView(generics.ListAPIView):
    
    def get(self,request):
        mark_choices = Mark.MARK_CHOICES
        quarter_choices = Mark.QUARTER_CHOICES
        type_choices = Mark.TYPE_CHOICES
        
        return Response({
            'mark_choices': mark_choices,
            'quarter_choices': quarter_choices,
            'type_choices': type_choices
        })

class StudentLessonList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    
    
    def get(self, request):
        
        user = request.user
        
        student_profile = StudentProfile.objects.get(user = user)
        student_class = StudentClass.objects.get(student = student_profile)
        student_lessons = SchoolLesson.objects.filter(teacherclasslesson__classes = student_class.class_num).distinct()
        serializer = SchoolLessonSerializer(student_lessons, many = True)
        
        return Response(serializer.data)
    
class StudentMarksList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        user = request.user
        
        student_profile = StudentProfile.objects.get(user=user)

        student_class = StudentClass.objects.filter(student=student_profile, class_num__current=True).select_related('class_num').first()
        
        if not student_class:
            return Response({'error': 'Класс не найден'}, status=status.HTTP_404_NOT_FOUND)
        
        student_lessons = SchoolLesson.objects.filter(teacherclasslesson__classes=student_class.class_num).distinct()
        
        marks = Mark.objects.filter(student=student_profile).select_related('lesson')
        
        marks_by_lesson = defaultdict(list)
        for mark in marks:
            marks_by_lesson[mark.lesson.id].append(mark)
        result = []
        
        for lesson in student_lessons:
            result.append({
                'lesson': lesson.name,
                'marks': MarkSerializer(marks_by_lesson[lesson.id], many=True).data
            })
            
        return Response(result)
    
class TeacherClassMarksView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, class_id, lesson_id):
        
        try:
            school_class = SchoolClass.objects.get(pk=class_id, current = True)
        except SchoolClass.DoesNotExist:
            return Response({'error': 'Класс не найден'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            class_lesson = SchoolLesson.objects.get(pk = lesson_id)
        except SchoolLesson.DoesNotExist:
            return Response({'errie': 'Предмет не найлен'}, status = status.HTTP_404_NOT_FOUND)
       
        student_links = StudentClass.objects.filter(class_num=school_class).select_related('student__user')
        
        students = [link.student for link in student_links]
        
        student_ids = [student.id for student in students]

        marks = Mark.objects.filter(student_id__in=student_ids, lesson = class_lesson).select_related('lesson', 'student__user')
        
        student_marks = defaultdict(list)
        for mark in marks:
            student_id = mark.student.id
            student_marks[student_id].append(MarkSerializer(mark).data)

        result = []
        for student in students:
            result.append({
                'student_name': student.user.get_full_name(),
                'student_id': student.id,
                'marks': student_marks[student.id]
            })

        return Response({
            'class': str(school_class),
            'lesson': class_lesson.name,
            'students': result
        })

   

class TeacherMarkPost(generics.CreateAPIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        user = request.user
        teacher = TeacherProfile.objects.get(user=user)
        lesson_id = request.data.get('lesson_id')
        mark_type = request.data.get('mark_type')
        value = request.data.get('value')
        student_id = request.data.get('student_id')

        student_classes = StudentClass.objects.filter(student__id=student_id).select_related('class_num')
        if not student_classes.exists():
            return Response({'error': 'Ученик не найден в классах'}, status=status.HTTP_400_BAD_REQUEST)
        current_student_class = max(student_classes, key=lambda sc: sc.class_num.date)
        school_class = current_student_class.class_num

        teacher_class_lesson = TeacherClassLesson.objects.filter(
            teacher=teacher,
            lesson__id=lesson_id,
            classes=school_class
        ).first()
        if not teacher_class_lesson:
            return Response({'error': 'Учитель не ведёт этот предмет в данном классе'}, status=status.HTTP_403_FORBIDDEN)

        mark = Mark.objects.create(
            student=current_student_class.student,
            teacher=teacher,
            lesson=teacher_class_lesson.lesson,
            quarter=currentQuarter(),
            mark_type=mark_type,
            value=value
        )
        return Response(MarkSerializer(mark).data, status=status.HTTP_201_CREATED)
