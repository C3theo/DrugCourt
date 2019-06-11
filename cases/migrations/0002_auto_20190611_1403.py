# Generated by Django 2.1.8 on 2019-06-11 18:03

from django.db import migrations, models
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referrals',
            name='dadecision',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Approved', 'Approved')], db_column='DADecision', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='referrals',
            name='defensedecision',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Approved', 'Approved')], db_column='DefenseDecision', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='referrals',
            name='pretrialdecision',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Approved', 'Approved')], db_column='PretrialDecision', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='referrals',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], db_column='Sex', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='referrals',
            name='status',
            field=django_fsm.FSMField(choices=[('Pending', 'Pending'), ('Pending Assessment', 'Pending Assessment'), ('Pending Client Acceptance', 'Pending Client Acceptance'), ('Rejected', 'Rejected'), ('Active', 'Active'), ('Terminated', 'Terminated'), ('Graduated', 'Graduated'), ('AWOL', 'AWOL'), ('Terminated', 'Terminated'), ('Medical Leave', 'Medical Leave'), ('Declined', 'Declined'), ('Rejected', 'Rejected'), ('In Custody', 'In Custody'), ('Pending Termination', 'Pending Termination')], db_column='Status', max_length=50),
        ),
        migrations.AlterField(
            model_name='referrals',
            name='teamdecision',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Approved', 'Approved')], db_column='TeamDecision', max_length=10, null=True),
        ),
    ]
