# Generated by Django 2.1.8 on 2019-07-09 21:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=20, unique=True)),
                ('status', django_fsm.FSMField(choices=[(0, 'Pending'), (1, 'Screening'), (2, 'In Program')], max_length=50)),
                ('created_date', models.DateTimeField(default=datetime.date.today)),
                ('birth_date', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Trans')], max_length=1)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_initial', models.CharField(max_length=1, null=True)),
                ('last_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'clients',
                'managed': True,
            },
            bases=(django_fsm.ConcurrentTransitionMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('clientid', models.CharField(db_column='ClientID', max_length=15, unique=True)),
                ('startdate', models.DateField(blank=True, db_column='StartDate', null=True)),
                ('dischargedate', models.DateField(blank=True, db_column='DischargeDate', null=True)),
                ('cellphone', models.CharField(blank=True, db_column='CellPhone', max_length=50, null=True)),
                ('email', models.EmailField(blank=True, db_column='Email', max_length=75, null=True)),
                ('message', models.CharField(blank=True, db_column='Message', max_length=50, null=True)),
                ('messagesource', models.CharField(blank=True, db_column='MessageSource', max_length=50, null=True)),
                ('yearlyincome', models.CharField(blank=True, db_column='YearlyIncome', max_length=20, null=True)),
                ('incomesource', models.CharField(blank=True, db_column='IncomeSource', max_length=25, null=True)),
                ('educationyrs', models.IntegerField(blank=True, db_column='EducationYrs', null=True)),
                ('educationlevel', models.CharField(blank=True, db_column='EducationLevel', max_length=50, null=True)),
                ('highschoolgrad', models.CharField(blank=True, db_column='HighSchoolGrad', max_length=3, null=True)),
                ('ged', models.CharField(blank=True, db_column='GED', max_length=3, null=True)),
                ('militaryservice', models.BooleanField(db_column='MilitaryService')),
                ('vaeligible', models.BooleanField(db_column='VAEligible')),
                ('maritalstatus', models.CharField(blank=True, db_column='MaritalStatus', max_length=20, null=True)),
                ('pregnant', models.CharField(blank=True, db_column='Pregnant', max_length=5, null=True)),
                ('children', models.CharField(blank=True, db_column='Children', max_length=12, null=True)),
                ('childnarrative', models.TextField(blank=True, db_column='ChildNarrative', null=True)),
                ('diagnosis', models.TextField(blank=True, db_column='Diagnosis', null=True)),
                ('suicide', models.BooleanField(db_column='Suicide')),
                ('violence', models.BooleanField(db_column='Violence')),
                ('health', models.TextField(blank=True, db_column='Health', null=True)),
                ('ghmedications', models.TextField(blank=True, db_column='GhMedications', null=True)),
                ('prenatal', models.TextField(blank=True, db_column='Prenatal', null=True)),
                ('tbstatus', models.CharField(blank=True, db_column='TBStatus', max_length=50, null=True)),
                ('physicalabuse', models.BooleanField(db_column='PhysicalAbuse')),
                ('sexualabuse', models.BooleanField(db_column='SexualAbuse')),
                ('insurance', models.CharField(blank=True, db_column='Insurance', max_length=50, null=True)),
                ('primarydrug', models.CharField(blank=True, db_column='PrimaryDrug', max_length=50, null=True)),
                ('substanceuse', models.CharField(blank=True, db_column='SubstanceUse', max_length=6, null=True)),
                ('sobriety', models.CharField(blank=True, db_column='Sobriety', max_length=50, null=True)),
                ('needleuse', models.BooleanField(db_column='NeedleUse')),
                ('addictionseverityindex', models.CharField(blank=True, db_column='AddictionSeverityIndex', max_length=50, null=True)),
                ('familyoforiginyn', models.BooleanField(db_column='FamilyofOriginYN')),
                ('familyoforiginuse', models.CharField(blank=True, db_column='FamilyofOriginUse', max_length=250, null=True)),
                ('spouseuseyn', models.BooleanField(db_column='SpouseUseYN')),
                ('spouseuse', models.CharField(blank=True, db_column='SpouseUse', max_length=250, null=True)),
                ('testtype', models.CharField(blank=True, db_column='TestType', max_length=50, null=True)),
                ('testresults', models.CharField(blank=True, db_column='TestResults', max_length=250, null=True)),
                ('employedatgraduation', models.BooleanField(blank=True, db_column='EmployedAtGraduation', null=True)),
                ('outcomecomments', models.TextField(blank=True, db_column='OutcomeComments', null=True)),
                ('cmuserid', models.CharField(blank=True, db_column='CMUserID', max_length=50, null=True)),
                ('couserid', models.CharField(blank=True, db_column='COUserID', max_length=50, null=True)),
                ('phase', models.CharField(blank=True, db_column='Phase', max_length=1, null=True)),
                ('stopbilling', models.BooleanField(blank=True, db_column='StopBilling', null=True)),
                ('userid', models.CharField(blank=True, db_column='UserID', max_length=50, null=True)),
                ('created', models.DateTimeField(blank=True, db_column='Created', null=True)),
                ('ssma_timestamp', models.TextField(db_column='SSMA_TimeStamp')),
                ('lastpositive', models.DateField(blank=True, db_column='LastPositive', null=True)),
                ('lep', models.IntegerField(blank=True, db_column='LEP', null=True)),
                ('employedatstart', models.CharField(blank=True, db_column='EmployedAtStart', max_length=12, null=True)),
                ('employedatgrad', models.CharField(blank=True, db_column='EmployedAtGrad', max_length=12, null=True)),
                ('asam_loc', models.DecimalField(blank=True, db_column='ASAM_LOC', decimal_places=1, max_digits=2, null=True)),
            ],
            options={
                'verbose_name_plural': 'clients',
                'db_table': 'Clients',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Enter notes here.')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('note_type', models.CharField(choices=[('Court', 'Court')], default='Court', max_length=25)),
                ('author', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.Profile')),
                ('client', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cases.Client')),
            ],
            options={
                'verbose_name_plural': 'notes',
                'db_table': 'Notes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('provider_type', models.CharField(choices=[('Treatment 1', 'Treatment 1')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', django_fsm.FSMField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')], max_length=20, verbose_name='Referral Status')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.Client')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.Provider')),
                ('referrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
            options={
                'permissions': [('can_approve', 'Can Approve Referral'), ('can_reject', 'Can Reject Referral')],
            },
            bases=(django_fsm.ConcurrentTransitionMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Referrals',
            fields=[
                ('refid', models.AutoField(db_column='RefID', primary_key=True, serialize=False)),
                ('clientid', models.CharField(db_column='ClientID', max_length=15, unique=True)),
                ('casenums', models.CharField(blank=True, db_column='CaseNums', max_length=255, null=True)),
                ('charges', models.CharField(blank=True, db_column='Charges', max_length=100, null=True)),
                ('spn', models.CharField(blank=True, db_column='SPN', max_length=8, null=True)),
                ('stateid', models.CharField(blank=True, db_column='StateID', max_length=15, null=True)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=20, null=True)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=20, null=True)),
                ('middlename', models.CharField(blank=True, db_column='MiddleName', max_length=20, null=True)),
                ('ssn', models.CharField(blank=True, db_column='SSN', max_length=11, null=True)),
                ('track', models.CharField(db_column='Track', max_length=1)),
                ('enrolldate', models.DateField(blank=True, db_column='EnrollDate', null=True)),
                ('rejectreason', models.CharField(blank=True, db_column='RejectReason', max_length=50, null=True)),
                ('dob', models.DateField(blank=True, db_column='DOB', null=True)),
                ('race', models.CharField(blank=True, db_column='Race', max_length=35, null=True)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], db_column='Sex', max_length=1, null=True)),
                ('status', django_fsm.FSMField(choices=[('Pending', 'Pending'), ('Pending Assessment', 'Pending Assessment'), ('Pending Client Acceptance', 'Pending Client Acceptance'), ('Rejected', 'Rejected'), ('Active', 'Active'), ('Terminated', 'Terminated'), ('Graduated', 'Graduated'), ('AWOL', 'AWOL'), ('Terminated', 'Terminated'), ('Medical Leave', 'Medical Leave'), ('Declined', 'Declined'), ('Rejected', 'Rejected'), ('In Custody', 'In Custody'), ('Pending Termination', 'Pending Termination')], db_column='Status', max_length=50)),
                ('division', models.IntegerField(blank=True, db_column='Division', null=True)),
                ('location', models.CharField(blank=True, db_column='Location', max_length=10, null=True)),
                ('cell', models.CharField(blank=True, db_column='Cell', max_length=10, null=True)),
                ('referredby', models.CharField(blank=True, db_column='ReferredBy', max_length=50, null=True)),
                ('referreddate', models.DateField(blank=True, db_column='ReferredDate', null=True)),
                ('pretrialname', models.CharField(blank=True, db_column='PretrialName', max_length=50, null=True)),
                ('pretrialreceived', models.DateField(blank=True, db_column='PretrialReceived', null=True)),
                ('pretrialcompleted', models.DateField(blank=True, db_column='PretrialCompleted', null=True)),
                ('pretrialdecision', models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')], db_column='PretrialDecision', max_length=10, null=True)),
                ('defensename', models.CharField(blank=True, db_column='DefenseName', max_length=50, null=True)),
                ('defensereceived', models.DateField(blank=True, db_column='DefenseReceived', null=True)),
                ('defensecompleted', models.DateField(blank=True, db_column='DefenseCompleted', null=True)),
                ('defensedecision', models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')], db_column='DefenseDecision', max_length=10, null=True)),
                ('daname', models.CharField(blank=True, db_column='DAName', max_length=50, null=True)),
                ('dareceived', models.DateField(blank=True, db_column='DAReceived', null=True)),
                ('dacompleted', models.DateField(blank=True, db_column='DACompleted', null=True)),
                ('dadecision', models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')], db_column='DADecision', max_length=10, null=True)),
                ('assessname', models.CharField(blank=True, db_column='AssessName', max_length=50, null=True)),
                ('assessreceived', models.DateField(blank=True, db_column='AssessReceived', null=True)),
                ('assesscompleted', models.DateField(blank=True, db_column='AssessCompleted', null=True)),
                ('teamreceived', models.DateField(blank=True, db_column='TeamReceived', null=True)),
                ('teamcompleted', models.DateField(blank=True, db_column='TeamCompleted', null=True)),
                ('teamdecision', models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')], db_column='TeamDecision', max_length=10, null=True)),
                ('arrests', models.IntegerField(blank=True, db_column='Arrests', null=True)),
                ('felonies', models.IntegerField(blank=True, db_column='Felonies', null=True)),
                ('misdemeanors', models.IntegerField(blank=True, db_column='Misdemeanors', null=True)),
                ('firstarrestyear', models.IntegerField(blank=True, db_column='FirstArrestYear', null=True)),
                ('created', models.DateTimeField(blank=True, db_column='Created', null=True)),
                ('userid', models.CharField(blank=True, db_column='UserID', max_length=50, null=True)),
                ('accepteddate', models.DateField(blank=True, db_column='AcceptedDate', null=True)),
                ('county', models.CharField(blank=True, db_column='County', max_length=50, null=True)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=25, null=True)),
                ('termreason', models.CharField(blank=True, db_column='TermReason', max_length=25, null=True)),
            ],
            options={
                'verbose_name_plural': 'referrals',
                'db_table': 'Referrals',
                'managed': True,
            },
            bases=(django_fsm.ConcurrentTransitionMixin, models.Model),
        ),
        migrations.AddField(
            model_name='provider',
            name='clients',
            field=models.ManyToManyField(through='cases.Referral', to='cases.Client'),
        ),
    ]
