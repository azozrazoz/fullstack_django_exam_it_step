# Generated by Django 5.0 on 2023-12-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_lessons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='online',
            field=models.BooleanField(),
        ),
    ]