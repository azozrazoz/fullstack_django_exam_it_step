# Generated by Django 5.0 on 2023-12-13 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_rename_ahievements_user_achievements'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Achievements',
            new_name='Achievement',
        ),
    ]
