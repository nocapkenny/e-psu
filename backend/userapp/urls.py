from django.urls import path

from userapp.views import TeacherList, TeacherDetail, StudentDetail

urlpatterns = [
    path('teachers/', TeacherList.as_view()),
    path('teachers/<int:pk>', TeacherDetail.as_view()),
    path('student/profile/', StudentDetail.as_view())
]