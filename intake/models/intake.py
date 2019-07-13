from datetime import date, datetime

from django.db import models
from django.db.models import F
from django.urls import reverse
from django.utils import timezone

from django_fsm import (ConcurrentTransitionMixin, FSMField,
                        TransitionNotAllowed, transition)
from profiles.models import Profile

tzinfo = timezone.get_current_timezone()


class IntakeStatus:

    STATUS_PENDING = 'Pending'
    STATUS_SCREEN = 'Screening'
    STATUS_ADMIT = 'In Program'

    CHOICES = (
        (0, STATUS_PENDING),
        (1, STATUS_SCREEN),
        (2, STATUS_ADMIT),
    )


class GenderOption:

    CHOICES = (('M', 'Male'),
               ('F', 'Female'), ('T', 'Trans'),)


class NoteOption(object):

    CHOICES = (('Court', 'Court'), )

# TODO:
# class EligibiltyCriteria:
#     pass

# class ScreenInstrument:
#     pass


class Client(ConcurrentTransitionMixin, models.Model):
    """
        Model to represent inital elgibility client information in a Drug Court Program
    """

    client_id = models.CharField(max_length=20, unique=True)
    status = FSMField(choices=IntakeStatus.CHOICES)
    created_date = models.DateTimeField(default=timezone.now)

    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GenderOption.CHOICES)
    first_name = models.CharField(max_length=20,)
    middle_initial = models.CharField(max_length=1, null=True)
    last_name = models.CharField(max_length=20,)

    def create_client_id(self):
        """
            Return unique id for client consisting of gender, birth date, SSN, and last name.
        """

        pre_text = date.today().year

        try:
            client_id = Client.objects.latest('client_id').client_id
            if client_id != '':
                latest_id = int(client_id)
                new_id = latest_id + 1
        except Client.DoesNotExist:
            new_id = f'{pre_text}000{1}'

        return new_id

    def save(self, *args, **kwargs):
        # import pdb
        # pdb.set_trace()

        if self.client_id == '':
            self.client_id = self.create_client_id()

        super().save(*args, **kwargs)

    @property
    def age(self):

        today = date.today()
        return (today.year - self.birth_date.year) - int(
            (today.month, today.day) <
            (self.birth_date.month, self.birth_date.day))

    def get_absolute_url(self):

        return reverse('referrals-update', kwargs={'pk': self.id})

    def __str__(self):
        return f'Client: {self.client_id}'

    class Meta:
        managed = True
        app_label = 'intake'
        verbose_name_plural = 'clients'

    # Conditions
    def screens_approved(self):
        # TODO: Have to query status of referral
        pass

    # Transitions
    @transition(field=status, source=IntakeStatus.STATUS_PENDING, target=IntakeStatus.STATUS_SCREEN,
                permission=lambda instance, user: user.has_perm('add_client'))
    def add_client(self):
        pass

    @transition(field=status, source=IntakeStatus.STATUS_SCREEN, target=IntakeStatus.STATUS_ADMIT,
                permission=lambda instance, user: user.has_perm())
    def eval_client(self):
        pass


# TODO: reactivate - issues with settings/ app_label
# class Provider(models.Model):

#     CHOICES = (('Treatment 1', 'Treatment 1'),
#                ('Treatment 2', 'Treatment 2'),
#                )

#     name = models.CharField(max_length=20,)
#     provider_type = models.CharField(max_length=20, choices=CHOICES)
#     # TODO: Change to actual types of treatment
#     # clients = models.ManyToManyField('intake.Client', through='Referral')

#     class Meta:
#         managed = True
#         app_label = 'intake'

    # TODO: Add more provider fields
    # location
    # services (method??)
    # other criterion for assessment


STATUS_PENDING = 'Pending'
STATUS_APPROVED = 'Approved'
STATUS_REJECTED = 'Rejected'

STATUS_CHOICES = ((0, STATUS_PENDING),
                  (1, STATUS_APPROVED),
                  (2, STATUS_REJECTED),)


class Decision(ConcurrentTransitionMixin, models.Model):
    """
        Model to represent decisions about client eligibility.
    """

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_received = models.DateTimeField()
    date_completed = models.DateTimeField()
    verdict = FSMField('Verdict', choices=STATUS_CHOICES,
                       max_length=20, default=0)
    referral = models.ForeignKey(
        'intake.Referral', on_delete=models.CASCADE)

    def get_absolute_url(self):
        pass

    class Meta:
        managed = True
        permissions = [('can_decide', 'Can Decide')
                       ]

    def one_decision_per_group(self, role):
        """
            FSM transition to check whether a decision from user's group has
            already been made.
        """
        # role = self.user.user_role
        decisions = Decision.objects.filter(
            referral=self.referral, user__user_role=role)
    
        return len(decisions.values_list()) == 1 
        # When this condition needs to be checked a user has not made decision (return value makes no sense)
        # seems like it should go with Referral status, but it does not have a user attribute (needed to check user role)
        # Needs to be passed in from view function

    @transition(field=verdict, source=STATUS_PENDING, target=STATUS_APPROVED,
                conditions=[one_decision_per_group], permission=lambda instance, user: user.has_perm('can_decide'))
    def approve(self):
        pass


class Referral(ConcurrentTransitionMixin, models.Model):
    """
        Model to represent the state of a Drug Court's Referrral for a specific client.
    """

    status = FSMField('Referral Status', choices=STATUS_CHOICES,
                      max_length=20, default=0)

    client = models.ForeignKey(
        'intake.Client', on_delete=models.CASCADE)
    referrer = models.ForeignKey(Profile, on_delete=models.CASCADE, default=0)
    # provider = models.ForeignKey(
    #     Provider, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Referral for {self.client}'

    class Meta:
        managed = True

    def screens_approved(self):
        # TODO: check decisions of all users assigned to referral
        pass

    def screens_rejected(self):
        # TODO: check all three
        pass

    @transition(field=status, source=STATUS_PENDING, target=STATUS_APPROVED, conditions=[screens_approved])
    def approve_referral(self):
        pass
        # TODO signals

    @transition(field=status, source=STATUS_PENDING, target=STATUS_REJECTED, conditions=[screens_rejected])
    def reject_referral(self):
        pass
        # TODO: add signals


class Note(models.Model):
    """
        Model to represent notes.

        Fields:
            note_type
    """
    # TODO: add logic to automatically create author from signed in user
    # pre_save signal??
    # need to make sure it's saved only once

    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, default=False)
    text = models.TextField(help_text='Enter notes here.')
    created_date = models.DateTimeField(default=timezone.now)
    note_type = models.CharField(
        choices=NoteOption.CHOICES, max_length=25, default='Court')

    # Many clients to one note
    # TODO: remove default after db reset
    client = models.ForeignKey(
        'intake.Client', on_delete=models.CASCADE)

    class Meta:
        managed = True
        app_label = 'intake'
        verbose_name_plural = 'notes'
