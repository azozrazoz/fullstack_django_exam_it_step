from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from authapp.models import *
from authapp.serializer import *

class UserView(APIView):
    def get(self, request):
        output = [ 
            { 
                "name": output.name, 
                "surname": output.surname,
                "age": output.age,
                "email": output.email,
                "group": output.group.__str__(),
                "achievements": output.achievements.__str__(),
            } for output in User.objects.all()
        ]
        
        for output in User.objects.all():
            print(output.achievements)

        return Response(output) 
    
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

class AchievementsView(APIView):
    def get(self, request):
        output = [ 
            { 
                'name': output.name,
            } for output in Achievement.objects.all()
        ]

        return Response(output) 
    
    
    def post(self, request):
        serializer = AchievementsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)