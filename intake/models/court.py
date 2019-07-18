from django.db import models
from django.db.models import F
from django.urls import reverse
from django.utils import timezone
from model_utils import Choices

from django_fsm import (ConcurrentTransitionMixin, FSMField,
                        TransitionNotAllowed, transition)


class CourtDate(models.Model):
    EVENT_CHOICES = Choices('Entry', 'Phase Appearance', 'Graduation', 'Termination', 'Special')
    TYPE_CHOICES = Choices('New', 'Review', 'Final')

    court_date_id = models.AutoField(db_column='CourtDateID', primary_key=True)

    client = models.ForeignKey('intake.Client', on_delete=models.CASCADE)

    court_date = models.DateField(db_column='CourtDate')

    event = models.CharField(max_length=50, choices=EVENT_CHOICES, blank=True, null=True)

    court_date_type = models.CharField(
        db_column='CourtDateType',choices=TYPE_CHOICES, max_length=10, blank=True, null=True)

    phase = models.ForeignKey(
        'intake.Phase', blank=True, null=True, on_delete=models.CASCADE)

    attendance = models.CharField(
        db_column='Attendance', max_length=50, blank=True, null=True)

    notes = models.ForeignKey(
        'intake.Note', blank=True, null=True, on_delete=models.CASCADE)

    # date_created = models.DateTimeField(autoadd=blank=True, null=True)
    # created_by

    class Meta:
        managed = True
        db_table = 'Court'

    def get_absolute_url(self):

        return reverse('intake:court-detail', kwargs={'pk': self.court_date_id})
