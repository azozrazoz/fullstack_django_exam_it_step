from django.shortcuts import render
from rest_framework.views import APIView
from .models import YouTubeVideo
from rest_framework.response import Response
from .serializer import *

class YouTubeVideoView(APIView):
    def get(self, request):
        output = [ 
            { 
                "title": output.title, 
                "channel": output.channel
            } for output in YouTubeVideo.objects.all()
        ]

        return Response(output) 
    
    def post(self, request):
        serializer = YouTubeVideoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
class StudentView(APIView):
    def get(self, request):
        output = [ 
            { 
                "id": output.id, 
                "avatar": output.avatar,
                "first_name": output.first_name,
                "last_name": output.last_name,
                "date_of_birth": output.date_of_birth,
                "email": output.email,
                "password": output.password,
                "specialization": output.specialization,
                "group_id": output.group_id,
                "training_course": output.training_course,
                "biography": output.biography,
                "achievements": output.achievements,
            } for output in Student.objects.all()
        ]

        return Response(output) 
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
class TeacherView(APIView):
    def get(self, request):
        output = [ 
            { 
                "id": output.id, 
                "avatar": output.avatar,
                "first_name": output.first_name,
                "last_name": output.last_name,
                "email": output.email,
                "password": output.password,
                "profession": output.profession,
                "lecture": output.lecture,
            } for output in Teacher.objects.all()
        ]

        return Response(output) 
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
class LessonView(APIView):
    def get(self, request):
        output = [ 
            { 
                "id": output.id, 
                "lesson_name": output.lesson_name,
                "group_id": output.group_id,
                "teacher_id": output.teacher_id,
            } for output in Lesson.objects.all()
        ]

        return Response(output) 
    
    def post(self, request):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
class GroupView(APIView):
    def get(self, request):
        output = [ 
            { 
                "id": output.id, 
                "group_name": output.group_name,
                "tutor_id": output.tutor_id,
            } for output in Group.objects.all()
        ]

        return Response(output) 
    
    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)       

class AchievementsView(APIView):
    def get(self, request):
        output = [ 
            { 
                "id": output.id, 
                "name": output.name,
            } for output in Achievements.objects.all()
        ]

        return Response(output) 
    
    def post(self, request):
        serializer = AchievementsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)       


