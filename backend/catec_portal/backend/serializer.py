from rest_framework import serializers
from backend.models import *

class YoutubeTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = youtube_test
        fields = (
            'title',
            'channel'
        )


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = (
            'name', 
            'date', 
            'lesson_type', 
            'title', 
            'group'
            'online'
            'start_time'
            'end_time'
        )
        