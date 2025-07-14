from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from schooltable.models import TeacherClassLesson, SchoolClass
from userapp.models import TeacherProfile
from schooltable.serializers import TeacherClassLessonSerializer, SchoolClassStudentsSerializer


class TeacherClassLessonsList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            teacher_profile = request.user.teacherprofile
        except TeacherProfile.DoesNotExist:
            raise PermissionDenied("Не учитель!")

        lessons = TeacherClassLesson.objects.filter(teacher=teacher_profile)
        serializer = TeacherClassLessonSerializer(lessons, many=True)
        return Response(serializer.data)


class TeacherClassLessonDetail(generics.RetrieveAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = SchoolClassStudentsSerializer
    queryset = SchoolClass.objects.all()
    



