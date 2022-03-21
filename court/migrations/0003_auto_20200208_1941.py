# Generated by Django 3.0.1 on 2020-02-09 00:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0002_auto_20200208_1941'),
        ('court', '0002_auto_20200126_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourtDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('court_date', models.DateField(db_column='court_date')),
                ('event', models.CharField(blank=True, choices=[('Entry', 'Entry'), ('Phase Appearance', 'Phase Appearance'), ('Graduation', 'Graduation'), ('Termination', 'Termination'), ('Special', 'Special')], max_length=50, null=True)),
                ('court_date_type', models.CharField(blank=True, choices=[('New', 'New'), ('Review', 'Review'), ('Final', 'Final')], db_column='CourtDateType', max_length=10, null=True)),
                ('phase', models.TextField(max_length=1)),
                ('attendance', models.CharField(blank=True, db_column='Attendance', max_length=50, null=True)),
                ('notes', models.TextField(max_length=15)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intake.Client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='Sanction',
            new_name='Sanctions',
        ),
        migrations.RenameModel(
            old_name='Screen',
            new_name='Screens',
        ),
        migrations.DeleteModel(
            name='CourtDate',
        ),
    ]