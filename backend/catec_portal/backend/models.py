from django.db import models

from authapp.models import Group

class youtube_test(models.Model):
    title = models.CharField(max_length=255)
    channel = models.CharField(max_length=255)
    
class Lessons(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    lesson_type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    group = models.ForeignKey(
        Group,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    online = models.BooleanField()
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    