# Generated by Django 2.1.8 on 2020-01-05 02:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=20, null=True, unique=True)),
                ('status', django_fsm.FSMField(blank=True, choices=[('Pending', 'Pending'), ('Screening', 'Screening'), ('In Program', 'In Program')], default='Pending', max_length=50, null=True, verbose_name='Client Status')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Trans')], max_length=1)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_initial', models.CharField(blank=True, max_length=1, null=True)),
                ('last_name', models.CharField(max_length=20)),
                ('ssn', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'clients',
                'managed': True,
            },
            bases=(django_fsm.ConcurrentTransitionMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CriminalBackground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrests', models.IntegerField(blank=True, db_column='Arrests', null=True)),
                ('felonies', models.IntegerField(blank=True, db_column='Felonies', null=True)),
                ('misdemeanors', models.IntegerField(blank=True, db_column='Misdemeanors', null=True)),
                ('firstarrestyear', models.IntegerField(blank=True, db_column='FirstArrestYear', null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intake.Client')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Decision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_by', models.CharField(choices=[('Drug Court Team', 'Drug Court Team'), ('DA', 'DA'), ('Defense', 'Defense'), ('Pretrial', 'Pretrial')], max_length=20, null=True)),
                ('date_received', models.DateField(blank=True, null=True)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('verdict', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20, verbose_name='Verdict')),
            ],
            options={
                'permissions': [('can_decide', 'Can Decide')],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Enter notes here.')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('note_type', models.CharField(blank=True, choices=[('Court', 'Court'), ('Treatment', 'Treatment'), ('General', 'General')], max_length=25, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_notes', to='intake.Client')),
            ],
            options={
                'verbose_name_plural': 'notes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase_id', models.CharField(blank=True, choices=[('Not in System', 'Not in System'), ('Phase One', 'Phase One'), ('Phase Two', 'Phase Two'), ('Phase Three', 'Phase Three')], max_length=20, null=True)),
                ('screens_per_week', models.IntegerField(default=1)),
                ('meetings_per_week', models.IntegerField(default=1)),
                ('fees', models.CharField(blank=True, max_length=4, null=True)),
                ('review_frequency', models.IntegerField(default=1)),
                ('notes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='intake.Note')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('provider_type', models.CharField(choices=[('Drug Court', 'Drug Court'), ('Other', 'Other')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', django_fsm.FSMField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Declined', 'Declined'), ('Active', 'Active'), ('In Custody', 'In Custody'), ('AWOL', 'AWOL'), ('Medical Leave', 'Medical Leave'), ('Pending Termination', 'Pending Termination'), ('Graduated', 'Graduated'), ('Terminated', 'Terminated'), ('Administrative Discharge', 'Administrative Discharge'), ('Deferred', 'Deferred')], default='Pending', max_length=20, verbose_name='Referral Status')),
                ('referrer', models.CharField(blank=True, max_length=20, null=True)),
                ('date_received', models.DateField(blank=True, null=True)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='intake.Client')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='intake.Provider')),
            ],
            options={
                'managed': True,
            },
            bases=(django_fsm.ConcurrentTransitionMixin, models.Model),
        ),
        migrations.AddField(
            model_name='provider',
            name='clients',
            field=models.ManyToManyField(through='intake.Referral', to='intake.Client'),
        ),
        migrations.AddField(
            model_name='decision',
            name='referral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intake.Referral'),
        ),
        migrations.AddField(
            model_name='client',
            name='phase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='intake.Phase'),
        ),
    ]
