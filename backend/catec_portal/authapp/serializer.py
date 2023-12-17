from rest_framework import serializers
from authapp.models import *

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'name',
        )
        
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            'name',
        )
        
        
class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            'name',
        )
        

class UserSerializer(serializers.ModelSerializer):
    achievements = serializers.ListField()
    
    class Meta:
        model = User
        fields = (
            'avatar',
            'name',
            'surname',
            'age',
            'email',
            'password',
            'phone',
            'group',
            'role',
            'time_update',
            'achievements',
        )

