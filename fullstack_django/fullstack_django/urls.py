from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from backend_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('youtube_test', YouTubeVideoView.as_view(), name='oh shit'),
    path('students', StudentView.as_view(), name='oh students'),
    path('teachers', TeacherView.as_view(), name='oh teachers'),
    path('lessons', LessonView.as_view(), name='oh lessons'),
    path('groups', GroupView.as_view(), name='oh groups'),
    path('achievements', AchievementsView.as_view(), name='oh achievements'),

    path("api/", include("user.urls")),
]
