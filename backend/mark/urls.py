from django.urls import path, include
from mark.views import StudentLessonList, StudentMarksList, TeacherClassMarksView, TeacherMarkPost, MarkChoisesView

urlpatterns = [
    path('student/lessons/', StudentLessonList.as_view()),
    path('student/marks/', StudentMarksList.as_view()),
    path('teacher/class/<int:class_id>/lesson/<int:lesson_id>', TeacherClassMarksView.as_view()),
    path('teacher/marks/post/', TeacherMarkPost.as_view()),
    path('teacher/marks/choices/', MarkChoisesView.as_view()),
]