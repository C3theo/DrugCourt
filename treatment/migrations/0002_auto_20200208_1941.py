# Generated by Django 3.0.1 on 2020-02-09 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0002_auto_20200208_1941'),
        ('treatment', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Objective',
            new_name='Objectives',
        ),
        migrations.RenameModel(
            old_name='ProbGoal',
            new_name='ProbGoals',
        ),
        migrations.RenameModel(
            old_name='Rating',
            new_name='Ratings',
        ),
        migrations.RenameModel(
            old_name='TxSession',
            new_name='TxAttendance',
        ),
    ]