from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from backend.models import *
from backend.serializer import *


class YouTubeVideoView(APIView):
    def get(self, request):
        output = [ 
            { 
                "title": output.title, 
                "channel": output.channel,
            } for output in youtube_test.objects.all()
        ]

        return Response(output) 
    
    
    def post(self, request):
        serializer = YoutubeTestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        


class LessonsView(APIView):
    def get(self, request):
        output = [ 
            { 
                'name': output.name,
                'date': output.date,
                'lesson_type': output.lesson_type, 
                'title': output.title, 
                'group': output.group.__str__(),
                'online': output.online,
                'start_time': output.start_time,
                'end_time': output.end_time,
            } for output in Lessons.objects.all()
        ]

        return Response(output) 
    
    
    def post(self, request):
        serializer = LessonsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

