from django.contrib import admin

from .models import Mark

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student_full_name', 'lesson', 'value', 'mark_type','date')
    list_filter = ('lesson', 'date', 'student', 'mark_type')
    search_fields = ('student__user__last_name', 'student__user__first_name', 'lesson__name')
    ordering = ('-date', 'student', 'lesson')

    def student_full_name(self, obj):
        return obj.student.user.get_full_name()
    student_full_name.short_description = 'ФИО Ученика'