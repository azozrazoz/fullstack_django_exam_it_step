# Generated by Django 5.0 on 2023-12-11 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users_avatars', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='authapp.group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='authapp.role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='time_update',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Последние изменение'),
        ),
    ]
