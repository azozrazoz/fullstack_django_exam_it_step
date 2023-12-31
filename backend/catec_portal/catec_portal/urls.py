"""
URL configuration for catec_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from backend.views import *
from authapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('youtube_test/', YouTubeVideoView.as_view(), name='oh shit'),
    path('users/', UserView.as_view(), name='oh shit users'),
    path('lessons/', LessonsView.as_view(), name='oh shit lessons'),
    path('achievements/', AchievementsView.as_view(), name='oh shit lessons'),
]
