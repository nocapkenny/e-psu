from django.urls import path, include

from schooltable.views import TeacherClassLessonsList, TeacherClassLessonDetail

urlpatterns = [
    
    path('teacher/classes/', TeacherClassLessonsList.as_view()),
    path('teacher/classes/<int:pk>', TeacherClassLessonDetail.as_view()),
    
]