# Generated by Django 2.1.8 on 2019-07-29 17:56

from django.db import migrations, models
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0008_auto_20190724_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='status',
            field=django_fsm.FSMField(blank=True, choices=[('Pending', 'Pending'), ('Screening', 'Screening'), ('In Program', 'In Program')], default='Pending', max_length=50, null=True, verbose_name='Client Status'),
        ),
        migrations.AlterField(
            model_name='decision',
            name='date_completed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='decision',
            name='date_received',
            field=models.DateField(blank=True, null=True),
        ),
    ]
