# Generated by Django 2.1.8 on 2020-01-27 02:14

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourtDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('court_date', models.DateField(db_column='court_date')),
                ('event', models.CharField(blank=True, choices=[('Entry', 'Entry'), ('Phase Appearance', 'Phase Appearance'), ('Graduation', 'Graduation'), ('Termination', 'Termination'), ('Special', 'Special')], max_length=50, null=True)),
                ('court_date_type', models.CharField(blank=True, choices=[('New', 'New'), ('Review', 'Review'), ('Final', 'Final')], max_length=10, null=True)),
                ('phase', models.TextField(max_length=1)),
                ('attendance', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.TextField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('bill_amt', models.IntegerField()),
                ('trans_date', models.DateField()),
                ('comments', models.TextField(max_length=15)),
                ('submitted', models.BooleanField()),
                ('submit_by', models.TextField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.CharField(blank=True, choices=[('Not in System', 'Not in System'), ('Phase One', 'Phase One'), ('Phase Two', 'Phase Two'), ('Phase Three', 'Phase Three')], max_length=20, null=True)),
                ('screens_per_week', models.IntegerField(default=1)),
                ('meetings_per_week', models.IntegerField(default=1)),
                ('review_frequency', models.IntegerField(default=1)),
                ('step_sessions', models.CharField(max_length=2)),
                ('site_num', models.CharField(max_length=30)),
                ('tx_hours', models.IntegerField()),
                ('min_days', models.IntegerField()),
                ('review_freq', models.CharField(max_length=30)),
                ('employment_hours', models.IntegerField()),
                ('fees', models.CharField(blank=True, max_length=4, null=True)),
                ('billing_amount', models.IntegerField()),
                ('billing_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PhaseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('phase', models.TextField(max_length=1)),
                ('total_days', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sanction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('sanc_desc', models.TextField(max_length=250)),
                ('jail_days', models.IntegerField()),
                ('comm_srvc_hrs', models.IntegerField()),
                ('comm_srvc_name', models.TextField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('result', models.TextField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
