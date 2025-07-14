from django.shortcuts import render

from rest_framework import generics, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from userapp.models import CustomUser, TeacherProfile, StudentProfile
from userapp.serializers import CustomUserSerlializer, TeacherProfileSerializer, StudentProfileSerializer


class TeacherList(generics.ListAPIView):
    
    serializer_class = TeacherProfileSerializer
    
    def get_queryset(self):
        return TeacherProfile.objects.filter(user__is_active = True)

class TeacherDetail(generics.RetrieveAPIView):
    
    serializer_class = TeacherProfileSerializer
        
    def get_queryset(self):
        return TeacherProfile.objects.filter(user__is_active = True)
           
class StudentDetail(generics.RetrieveAPIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        try:
            student_profile = StudentProfile.objects.get(user=user)
        except StudentProfile.DoesNotExist:
            return Response({"error": "Student profile not found"}, status = status.HTTP_404_NOT_FOUND)
        
        serializer = StudentProfileSerializer(student_profile)
        return Response(serializer.data)
    
