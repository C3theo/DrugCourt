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
            latest_id = int(Client.objects.latest('client_id').client_id)
            new_id = latest_id + 1
        except Client.DoesNotExist:
            new_id = f'{pre_text}000{1}'

        return new_id

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
        app_label = 'cases'
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


class Provider(models.Model):

    CHOICES = (('Treatment 1', 'Treatment 1'), )

    name = models.CharField(max_length=20,)
    provider_type = models.CharField(max_length=20, choices=CHOICES)
    # TODO: Change to actual types of treatment
    clients = models.ManyToManyField(Client, through='Referral')

    class Meta:
        managed = True

    # TODO: Add more provider fields
    # location
    # services (method??)
    # other criterion for assessment


class Referral(ConcurrentTransitionMixin, models.Model):
    """
        Model to represent the state of a Drug Court's Referrral for a specific client.
    """

    STATUS_PENDING = 'Pending'
    STATUS_APPROVED = 'Approved'
    STATUS_REJECTED = 'Rejected'

    CHOICES = ((0, STATUS_PENDING),
               (1, STATUS_APPROVED),
               (2, STATUS_REJECTED),)

    status = FSMField('Referral Status', choices=CHOICES, max_length=20,)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    referrer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.client} {self.provider}'

    class Meta:
        permissions = [('can_approve', 'Can Approve Referral'),
                       ('can_reject', 'Can Reject Referral'),
                       ]

    def screens_approved(self):
        # TODO: check decisions of all users assigned to referral
        pass

    def screens_rejected(self):
        # TODO: check all three
        pass

    @transition(field=status, source=STATUS_PENDING, target=STATUS_APPROVED, conditions=[screens_approved],
                permission=lambda instance, user: user.has_perm('can_approve'))
    def approve_referral(self):
        pass
        # TODO signals

    @transition(field=status, source=STATUS_PENDING, target=STATUS_REJECTED, conditions=[screens_rejected],
                permission=lambda instance, user: user.has_perm('can_reject'))
    def reject_referral(self):
        pass
        # TODO: add signals

    
    class Meta:
        managed = True



class Note(models.Model):
    """
        Model to represent user notes
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
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, null=True, default=False)

    class Meta:
        managed = True
        db_table = 'Notes'
        verbose_name_plural = 'notes'
