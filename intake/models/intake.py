from datetime import date, datetime

from django.db import models
from django.db.models import F
from django.urls import reverse
from django.utils import timezone
from model_utils import Choices


from django_fsm import (ConcurrentTransitionMixin, FSMField,
                        TransitionNotAllowed, transition)
from profiles.models import Profile
from .bpmn import Phase, Decision

tzinfo = timezone.get_current_timezone()


class IntakeStatus:

    STATUS_PENDING = 'Pending'
    STATUS_SCREEN = 'Screening'
    STATUS_ADMIT = 'In Program'

    CHOICES = Choices(STATUS_PENDING, STATUS_SCREEN, STATUS_ADMIT)


class GenderOption:

    CHOICES = (('M', 'Male'),
               ('F', 'Female'), ('T', 'Trans'),)


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
    ssn = models.CharField(max_length=20, null=True, blank=True)
    phase = models.ForeignKey(
        'intake.Phase', on_delete=models.CASCADE, blank=True, null=True)

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

        return reverse('intake:detail', kwargs={'pk': self.id})

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


class Referral(ConcurrentTransitionMixin, models.Model):
    """
        Model to represent the state of a Drug Court's Referrral for a specific client.
    """
    STATUS_PENDING = 'Pending'
    STATUS_APPROVED = 'Approved'
    STATUS_REJECTED = 'Rejected'

    STATUS_CHOICES = Choices(STATUS_PENDING, STATUS_APPROVED, STATUS_REJECTED)

    status = FSMField('Referral Status',
                      max_length=20, default=STATUS_PENDING)

    client = models.ForeignKey(
        'intake.Client', on_delete=models.CASCADE)
    referrer = models.CharField(max_length=20, null=True, blank=True)
    # referrer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    provider = models.ForeignKey(
        'intake.Provider', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Referral for {self.client}'

    class Meta:
        managed = True

    def all_decisions_approved(self):
        decision_count = Decision.objects.filter(referral=self).count()
        return decision_count == 3

    def screens_rejected(self):
        # TODO: check all three
        pass

    @transition(field=status, source=STATUS_PENDING, target=STATUS_APPROVED, conditions=[all_decisions_approved])
    def approve_referral(self):
        p = Phase(phase_id='Phase One')
        p.save()
        self.client.phase = p
        self.client.save()

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

    CHOICES = Choices('Court', 'Treatment', 'General')
    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(help_text='Enter notes here.')
    created_date = models.DateTimeField(auto_now_add=True)
    note_type = models.CharField(
        choices=CHOICES, max_length=25, default='Court')

    # Many clients to one note
    # TODO: remove default after db reset
    client = models.ForeignKey(
        'intake.Client', related_name='client_notes', on_delete=models.CASCADE)

    class Meta:
        managed = True
        app_label = 'intake'
        verbose_name_plural = 'notes'

    def __str__(self):
        return f'Note: {self.client.client_id}'


class CriminalBackground(models.Model):
    client = models.ForeignKey('intake.Client', on_delete=models.CASCADE)
    arrests = models.IntegerField(db_column='Arrests', blank=True, null=True)
    felonies = models.IntegerField(db_column='Felonies', blank=True, null=True)
    misdemeanors = models.IntegerField(
        db_column='Misdemeanors', blank=True, null=True)
    firstarrestyear = models.IntegerField(
        db_column='FirstArrestYear', blank=True, null=True)

    def __str__(self):
            return f'CriminalBackGround: {self.client.client_id}'
