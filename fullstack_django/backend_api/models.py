from django.db import models

# Create your models here.

class YouTubeVideo(models.Model):
    title = models.CharField(max_length=255)
    channel = models.CharField(max_length=255)

class Teacher(models.Model):
    avatar = models.ImageField(
        upload_to='users_avatars',
        blank=True,
        verbose_name='аватар',
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profession = models.CharField(max_length=255, blank=True)
    lecture = models.CharField(max_length=255, blank=True)

class Group(models.Model):
    group_name = models.CharField(max_length=255)
    tutor = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
    )

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=255)
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
    )

class Achievements(models.Model):
    name = models.CharField(max_length=255)

class Student(models.Model):
    avatar = models.ImageField(
        upload_to='users_avatars',
        blank=True,
        verbose_name='аватар',
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(auto_now_add=True)
    time_create = models.DateField(auto_now_add=True)         
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255, blank=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
    )
    training_course = models.CharField(max_length=255, blank=True)
    biography = models.CharField(max_length=255, blank=True)
    achievements = models.ManyToManyField(
        Achievements,
    )

class Marks(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        null=True,
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    mark = models.FloatField()
