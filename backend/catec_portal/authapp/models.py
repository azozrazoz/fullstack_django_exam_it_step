from django.db import models
from django.contrib.auth.models import AbstractUser


class Group(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Role(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Achievement(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    
class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='users_avatars',
        blank=True,
        null=True,
        verbose_name='Аватар',
    )
    name = models.CharField(
        verbose_name='Имя',
        max_length=255,
    )
    surname = models.CharField(
        verbose_name='Фамилия',
        max_length=255,
    )
    age = models.PositiveIntegerField(
        verbose_name='Возраст',
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name='Почта',
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=255,
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=255,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Группа',
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    time_update = models.DateTimeField(
        verbose_name='Последние изменение',
        auto_now_add=True,
    )
    achievements = models.ManyToManyField(Achievement, related_name="achievements", blank=True)
    

