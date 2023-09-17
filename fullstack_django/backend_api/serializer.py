from rest_framework import serializers
from .models import YouTubeVideo, Teacher, Student, Lesson, Group, Achievements

class YouTubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeVideo
        fields = ['title', 'channel']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
                  'avatar',
                  'first_name',
                  'last_name',
                  'date_of_birth',
                  'email',
                  'password',
                  'specialization',
                  'group_id',
                  'training_course',
                  'biography',
                  'achievements',
                 ]

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
                  'avatar',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'profession',
                  'lecture',
                 ]

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
                  'lesson_name',
                  'group_id',
                  'teacher_id',
                 ]
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
                  'group_name',
                  'tutor_id',
                 ]
        
        
class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = [
                  'name',
                 ]