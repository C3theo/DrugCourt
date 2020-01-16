# Generated by Django 3.0.1 on 2020-01-11 21:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('intake', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objectives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('description', models.TextField(max_length=250)),
                ('obj_num', models.IntegerField()),
                ('obj_target', models.DateField()),
                ('closed', models.BooleanField()),
                ('met', models.BooleanField()),
                ('met_date', models.DateField()),
                ('tx_rating', models.IntegerField()),
                ('client_rating', models.IntegerField()),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='intake.Client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProbGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('prob_description', models.TextField(max_length=250)),
                ('goal_description', models.TextField(max_length=250)),
                ('prob_goal_num', models.IntegerField()),
                ('prob_goal_target', models.DateField()),
                ('prob_goal_status', models.CharField(choices=[('Active', 'Active'), ('Maintenance', 'Maintenance'), ('Referred', 'Referred'), ('Referred to Case Mgmt', 'Referred to Case Mgmt'), ('Deferred', 'Deferred'), ('Resolved', 'Resolved'), ('Refused', 'Refused')], max_length=25)),
                ('status_date', models.DateField()),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='intake.Client')),
                ('objective', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='treatment.Objectives')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TxProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
                ('problems', models.TextField(max_length=250)),
                ('next_review', models.DateField()),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='intake.Client')),
                ('note', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='intake.Note')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TxAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('session_date', models.DateField()),
                ('attended', models.BooleanField()),
                ('absence_reason', models.CharField(choices=[('Absent', 'Absent'), ('Late', 'Late'), ('Excused', 'Excused'), ('Medical', 'Medical')], max_length=25)),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='intake.Client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('rating_date', models.DateField()),
                ('item_description', models.TextField(max_length=250)),
                ('staff_rating', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], max_length=1)),
                ('client_rating', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], max_length=1)),
                ('client_obj_number', models.IntegerField()),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='intake.Client')),
                ('obj_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='treatment.Objectives')),
                ('prob_goal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='treatment.ProbGoals')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]