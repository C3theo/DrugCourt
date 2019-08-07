from datetime import date, datetime

from django.db import models
from django.db.models import F
from django.urls import reverse
from django.utils import timezone
from model_utils import Choices


from django_fsm import (ConcurrentTransitionMixin, FSMField,
                        TransitionNotAllowed, transition)

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

    client_id = models.CharField(max_length=20, unique=True, null=True)
    status = FSMField('Client Status', choices=IntakeStatus.CHOICES,
                      default=IntakeStatus.STATUS_PENDING, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GenderOption.CHOICES)
    first_name = models.CharField(max_length=20,)
    middle_initial = models.CharField(max_length=1, null=True, blank=True)
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
        """
            Create ClientID when Client created
        """
        # TODO: Fix bug where Client is saved over
        
        if not self.client_id:
            self.client_id = self.create_client_id()

        super().save(*args, **kwargs)

    @property
    def age(self):

        today = date.today()
        return (today.year - self.birth_date.year) - int(
            (today.month, today.day) <
            (self.birth_date.month, self.birth_date.day))

    @property
    def full_name(self):
        return f'{self.first_name} {self.middle_initial}. {self.last_name}'

    def get_absolute_url(self):

        return reverse('intake:client-detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.client_id}'

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


class Referral(ConcurrentTransitionMixin, models.Model):
    """
        Model to represent the state of a Drug Court's Client Referrral process.
    """

    STATUS_PENDING = 'Pending'
    STATUS_APPROVED = 'Approved'
    STATUS_REJECTED = 'Rejected'

    STATUS_CHOICES = Choices(STATUS_PENDING, STATUS_APPROVED, STATUS_REJECTED)
    status = FSMField('Referral Status',
                      max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    client = models.ForeignKey(
        'intake.Client', on_delete=models.CASCADE, blank=True, null=True)
    referrer = models.CharField(max_length=20, null=True, blank=True)
    # TODO: add referrer ForeignKey later
    # referrer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    provider = models.ForeignKey(
        'intake.Provider', on_delete=models.CASCADE, null=True, blank=True)
    date_received = models.DateField(null=True, blank=True)
    date_completed = models.DateField(null=True, blank=True)

    @property
    def decisions(self):
        return self.decision_set.all()

    @property
    def decision_count(self):
        return self.decision_set.all().count()

    def save(self, commit=False, *args, **kwargs):
        """
            Create Decision objects upon Referral creation
        """

        super().save(*args, **kwargs)

        if not self.decisions_created():
            dc_decision = Decision.objects.create(
                referral=self, made_by=Decision.ROLE_DC)
            da_decision = Decision.objects.create(
                referral=self, made_by=Decision.ROLE_DA)
            pretrial_decision = Decision.objects.create(
                referral=self, made_by=Decision.ROLE_PRETRIAL)
            dc_decision.save()
            da_decision.save()
            pretrial_decision.save()
            
        # try:
        #     self.approve_referral()
        # except TransitionNotAllowed:
        #     pass
            # TODO: send messsage

        # TODO: add checks to see if there are more or less than required decisions

    def get_absolute_url(self):
        return reverse('intake:referral-detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'ReferralID:{self.id} - ClientID: {self.client}'

    class Meta:
        managed = True

    def all_decisions_approved(self):
        return self.decision_set.filter(verdict='Approved').count() == 3

    def decisions_created(self):
        return self.decision_count == 3

    def screens_rejected(self):
        # TODO: check if it needs to be all three or single rejection
        raise(NotImplementedError)

    @transition(field=status, source=STATUS_PENDING, target=STATUS_APPROVED, conditions=[all_decisions_approved])
    def approve(self):
        """
            Add Client to Phase when all Decisions approved
        """
        p = Phase(phase_id='Phase One')
        p.save()
        self.client.phase = p
        self.client.save()

    @transition(field=status, source=STATUS_PENDING, target=STATUS_REJECTED, conditions=[screens_rejected])
    def reject_referral(self):
        pass
        # TODO: add signals


class Decision(models.Model):
    """
        Model to represent decisions about client eligibility.
    """
    STATUS_PENDING = 'Pending'
    STATUS_APPROVED = 'Approved'
    STATUS_REJECTED = 'Rejected'

    STATUS_CHOICES = Choices(STATUS_PENDING, STATUS_APPROVED, STATUS_REJECTED)

    ROLE_DC = 'Drug Court Team'
    ROLE_DA = 'DA'
    ROLE_DEFENSE = 'Defense'
    ROLE_PRETRIAL = 'Pretrial'
    ROLES = Choices(ROLE_DC, ROLE_DA, ROLE_DEFENSE, ROLE_PRETRIAL)

    # user = models.ForeignKey(
    #     Profile, null=True, blank=True, on_delete=models.CASCADE)
    made_by = models.CharField(max_length=20, choices=ROLES, null=True)
    date_received = models.DateField(null=True, blank=True)
    date_completed = models.DateField(null=True, blank=True)
    verdict = models.CharField('Verdict', choices=STATUS_CHOICES,
                       max_length=20, default=STATUS_PENDING)
    referral = models.ForeignKey(
        'intake.Referral', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('intake:referral-detail', kwargs={'pk': self.referral.id})

    def __str__(self):
        return f"{self.made_by} Decision for Client{self.referral.client.client_id}"

    class Meta:
        managed = True
        permissions = [('can_decide', 'Can Decide')]


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


class CriminalBackground(models.Model):
    """
        Client Arrest History
    """
    client = models.ForeignKey('intake.Client', on_delete=models.CASCADE)
    arrests = models.IntegerField(db_column='Arrests', blank=True, null=True)
    felonies = models.IntegerField(db_column='Felonies', blank=True, null=True)
    misdemeanors = models.IntegerField(
        db_column='Misdemeanors', blank=True, null=True)
    firstarrestyear = models.IntegerField(
        db_column='FirstArrestYear', blank=True, null=True)

    def __str__(self):
        return f'CriminalBackGround - Client: {self.client.client_id}'

    class Meta:
        managed = True

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
