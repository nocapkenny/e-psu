from django.contrib import admin
from schooltable.models import StudentClass, SchoolClass, SchoolLesson, TeacherClassLesson

@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    list_display = ('student_full_name', 'class_name', 'class_year')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'class_num__name')
    list_filter = ('class_num__name', 'class_num__date')
    ordering = ('-class_num__date',)

    def student_full_name(self, obj):
        return f"{obj.student.user.last_name} {obj.student.user.first_name}"
    student_full_name.short_description = 'Ученик'

    def class_name(self, obj):
        return obj.class_num.name
    class_name.short_description = 'Класс'

    def class_year(self, obj):
        return obj.class_num.date
    class_year.short_description = 'Год'
    
@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_filter = ('date',)
    ordering = ('-date',)
    
    
@admin.register(SchoolLesson)
class lessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
@admin.register(TeacherClassLesson)
class TeacherClassLessonAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'lesson', 'classes')
    list_filter = ('lesson', 'classes')
    ordering = ('-classes',)
    search_fields = ('teacher__user_first_name', 'teacher__user_last_name')