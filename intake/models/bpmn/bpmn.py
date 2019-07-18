from viewflow import flow
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from django.db import models
from viewflow.models import Process
from model_utils import Choices

from profiles.models import Profile

from django_fsm import (ConcurrentTransitionMixin, FSMField,
                        TransitionNotAllowed, transition)


class DynamicSplitProcess(Process):
    split_count = models.IntegerField(default=0)


class Decision(models.Model):
    """
        Model to represent decisions about client eligibility.
    """
    STATUS_PENDING = 'Pending'
    STATUS_APPROVED = 'Approved'
    STATUS_REJECTED = 'Rejected'

    STATUS_CHOICES = Choices(STATUS_PENDING, STATUS_APPROVED, STATUS_REJECTED)

    user = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    date_received = models.DateField()
    date_completed = models.DateField()
    verdict = FSMField('Verdict', choices=STATUS_CHOICES,
                       max_length=20, default=0)
    referral = models.ForeignKey(
        'intake.Referral', on_delete=models.CASCADE)

    def get_absolute_url(self):
        pass

    class Meta:
        managed = True
        permissions = [('can_decide', 'Can Decide')]

    def one_decision_per_role(self):
        """
            FSM transition to check whether a decision from user's group has
            already been made.
        """
        role = self.user.user_role
        decisions = Decision.objects.filter(
            referral=self.referral, user__user_role=role)

        return len(decisions.values_list()) == 0

    @transition(field=verdict, source=STATUS_PENDING, target=STATUS_APPROVED,
                conditions=[one_decision_per_role], permission=lambda instance, user: user.has_perm('can_decide'))
    def approve(self):
        pass


class Phase(models.Model):
    """
    """
    CHOICES = Choices('Not in System', 'Phase One', 'Phase Two', 'Phase Three')

    phase_id = models.CharField(
        max_length=20, choices=CHOICES, null=True, blank=True)
    screens_per_week = models.IntegerField(default=1)
    meetings_per_week = models.IntegerField(default=1)
    fees = models.CharField(max_length=4, null=True, blank=True)
    notes = models.ForeignKey('intake.Note', null=True,
                              blank=True, on_delete=models.CASCADE)
    review_frequency = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.phase_id}'


class HelloWorldProcess(Process):
    text = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)
