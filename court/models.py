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
    EVENT_CHOICES = Choices('Entry', 'Phase Appearance',
                            'Graduation', 'Termination', 'Special')
    TYPE_CHOICES = Choices('New', 'Review', 'Final')

    client = models.ForeignKey('intake.client', on_delete=models.CASCADE)

    court_date = models.DateField(db_column='court_date')

    event = models.CharField(
        max_length=50, choices=EVENT_CHOICES, blank=True, null=True)

    court_date_type = models.CharField(
        db_column='CourtDateType', choices=TYPE_CHOICES, max_length=10, blank=True, null=True)

    phase = models.TextField(max_length=1)

    attendance = models.CharField(
        db_column='Attendance', max_length=50, blank=True, null=True)

    notes = models.TextField(max_length=15)

    # date_created = models.DateTimeField(autoadd=blank=True, null=True)
    # created_by
    # def get_absolute_url(self):
    #     return reverse('court:detail', kwargs={'pk': self.id})


class Phase(TimeStampedModel):
    # contains phase info setup by Coordinator

    FREQUENCY = Choices('Weekly', 'Biweekly', 'Monthly')
    CHOICES = Choices('1', '2', '3', '4', '5')

    site_num = models.CharField(max_length=1)
    phase = models.CharField(max_length=1)
    screens_per_week = models.IntegerField(default=1)
    meetings_per_week = models.IntegerField(default=1)
    review_frequency = models.CharField(max_length=10, choices=FREQUENCY)
    step_sessions = models.IntegerField()
    tx_sessions = models.IntegerField()
    tx_hours = models.IntegerField()
    min_phase_days = models.IntegerField()
    weekly_employment_hours = models.IntegerField()  # Client Required Hours
    phase_id = models.IntegerField()
    billing_amount = models.IntegerField()
    billing_total = models.IntegerField()

    # Other = models.IntegerField()
    def __str__(self):
        return f'{self.phase_id}'


class FeeHistory(TimeStampedModel):
    """
        Financial History of all Client transactions
    """
    client = models.ForeignKey(
        'intake.Client', on_delete=models.CASCADE, blank=True, null=True)
    bill_amt = models.IntegerField()
    trans_date = models.DateField()
    comments = models.TextField(max_length=15)  # money order/check
    submitted = models.BooleanField()
    submit_by = models.TextField(max_length=15)
    submit_date = models.DateField


class PhaseHistory(TimeStampedModel):
    client = models.ForeignKey(
        'intake.Client', on_delete=models.CASCADE, blank=True, null=True)
    phase = models.TextField(max_length=1)
    completed = models.BooleanField
    total_days = models.IntegerField()


class Screens(TimeStampedModel):
    client = models.ForeignKey(
        'intake.Client', on_delete=models.CASCADE, blank=True, null=True)
    collect_date = models.DateField
    test_date = models.DateField
    result = models.TextField(max_length=250)
    result_confirmed = models.BooleanField
    positive_approved = models.BooleanField


class Sanctions(TimeStampedModel):
    client = models.ForeignKey(
        'intake.Client', on_delete=models.CASCADE, blank=True, null=True)
    sanc_date = models.DateField
    sanc_desc = models.TextField(max_length=250)
    jail_days = models.IntegerField()
    jail_start = models.DateField
    Jail_end = models.DateField
    comm_srvc_hrs = models.IntegerField()
    Comm_srv_start = models.DateField
    comm_srv_end = models.DateField
    comm_srvc_name = models.TextField(max_length=15)
