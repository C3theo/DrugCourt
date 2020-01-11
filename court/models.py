# Create your models here.
from django.db import models
from django.db.models import F
from django.urls import reverse
from django.utils import timezone
from model_utils import Choices
from model_utils.models import TimeStampedModel 

from django_fsm import (ConcurrentTransitionMixin, FSMField,
                        TransitionNotAllowed, transition)


class CourtDates(TimeStampedModel):
    EVENT_CHOICES = Choices('Entry', 'Phase Appearance', 'Graduation', 'Termination', 'Special')
    TYPE_CHOICES = Choices('New', 'Review', 'Final')
    court_date_ID = models.IntegerField(primary_key = True)
    client_ID = models.ForeignKey('intake.client', on_delete=models.CASCADE)

    court_date = models.DateField(db_column='court_date')

    event = models.CharField(max_length=50, choices=EVENT_CHOICES, blank=True, null=True)

    court_date_type = models.CharField(
        db_column='CourtDateType', choices=TYPE_CHOICES, max_length=10, blank=True, null=True)

    phase = models.TextField(max_length=1)

    attendance = models.CharField(
        db_column='Attendance', max_length=50, blank=True, null=True)

    notes = models.TextField(max_length=15)

    # date_created = models.DateTimeField(autoadd=blank=True, null=True)
    # created_by

    class Meta:
        managed = True
        db_table = 'CourtDates'

    #def get_absolute_url(self):

    #    return reverse('court:court-detail', kwargs={'pk': self.court_date_ID})

class PhaseParms(models.Model):
    Phase = models.CharField(max_length=1)
    SiteNum = models.CharField(max_length=30)
    Screens = models.CharField(max_length=1)
    StepSessions = models.CharField(max_length=2)
    MtgsPerWeek = models.CharField(max_length=1)
    CourtFrequency = Choices('Weekly', 'Biweekly', 'Monthly')
    TxSessionHrs = models.IntegerField()
    Other = models.IntegerField()
    MinPhaseDays = models.IntegerField()
    CaseReviewFreq = models.CharField(max_length=30)
    BillingAmount = models.IntegerField()
    BillingTotal = models.IntegerField()
    EmploymentHrs = models.IntegerField()

class Fees(TimeStampedModel):                                             
    client_ID = models.TextField(max_length=15)
    bill_amt = models.IntegerField()    
    trans_date = models.DateField
    comments = models.TextField(max_length=15)
    submitted = models.BooleanField
    submit_by= models.TextField(max_length=15) 
    submit_date = models.DateField

class ClientPhases(TimeStampedModel):
    client_ID= models.TextField(max_length=15)
    phase = models.TextField(max_length=1)
    completed = models.BooleanField
    total_days = models.IntegerField()

class Screens(TimeStampedModel):
    client_ID = models.TextField(max_length=15)
    collect_date = models.DateField
    test_date = models.DateField
    result = models.TextField(max_length=250)
    result_confirmed = models.BooleanField
    positive_approved = models.BooleanField

class Sanctions(TimeStampedModel):
    client_ID= models.TextField(max_length=15)
    sanc_date = models.DateField
    sanc_desc= models.TextField(max_length=250)
    jail_days = models.IntegerField()
    Jail_start = models.DateField 
    Jail_end = models.DateField
    comm_srvc_hrs = models.IntegerField()
    Comm_srv_start = models.DateField
    comm_srv_end = models.DateField
    comm_srvc_name = models.TextField(max_length=15)
