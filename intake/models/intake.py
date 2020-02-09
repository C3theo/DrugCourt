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
    STATUS_ACCEPTED = 'Accepted'

    CHOICES = Choices(
        (STATUS_PENDING, STATUS_PENDING),
        (STATUS_SCREEN, STATUS_SCREEN),
        (STATUS_ACCEPTED, STATUS_ACCEPTED),

    )


class ClientStatus:

    Choices = Choices(
        ('Active', 'Active'),
        ('Declined', 'Declined'),
        ('In Custody', 'In Custody'),
        ('AWOL', 'AWOL'),
        ('Medical Leave', 'Medical Leave'),
        ('Pending Termination', 'Pending Termination'),
        ('Graduated', 'Graduated'),
        ('Terminated', 'Terminated'),
        ('Administrative Discharge', 'Administrative Discharge'),
        ('Deferred', 'Deferred')
    )


class GenderOption:

    CHOICES = (('M', 'Male'),
               ('F', 'Female'), ('T', 'Trans'),)


class Client(ConcurrentTransitionMixin, models.Model):
    """
        Model to represent inital eligibility criterion
    """

    client_id = models.CharField(max_length=100, unique=True, null=True)
    status = FSMField('Client Status', choices=IntakeStatus.CHOICES,
                      default=IntakeStatus.STATUS_PENDING, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GenderOption.CHOICES)
    first_name = models.CharField(max_length=20,)
    middle_initial = models.CharField(max_length=1, blank=True)
    last_name = models.CharField(max_length=20,)
    ssn = models.CharField(max_length=20, null=True, blank=True)
    phase = models.ForeignKey(
        'court.Phase', on_delete=models.CASCADE, blank=True, null=True)

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
            new_id = f'{pre_text}{1}'

        return new_id

    def save(self, *args, **kwargs):
        """
            Create ClientID when Client model first created.
        """

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
        return f'{self.full_name}'

    class Meta:

        app_label = 'intake'
        verbose_name_plural = 'clients'


class Referral(ConcurrentTransitionMixin, models.Model):
    """
        Model to represent the state of a client during Referrral process.
    """

    STATUS_PENDING = 'Pending'
    STATUS_APPROVED = 'Approved'
    STATUS_REJECTED = 'Rejected'

    STATUS_CHOICES = Choices(
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )

    status = FSMField('Referral Status',
                      max_length=40, choices=STATUS_CHOICES, default=STATUS_PENDING)
    client = models.OneToOneField(
        'intake.Client', on_delete=models.CASCADE, blank=True, null=True)
    referrer = models.CharField(max_length=20, null=True, blank=True)
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
            Create Decision objects upon Referral creation.
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

    def get_absolute_url(self):
        return reverse('intake:update', kwargs={'pk': self.id})

    def __str__(self):
        return f'ReferralID:{self.id} - ClientID: {self.client}'

    def approve_all_decisions(self):
        for each in self.decisions:
            each.verdict = Decision.STATUS_CHOICES['Approved']
            each.save()

    ### Transition Conditions ###

    def all_decisions_approved(self):
        """
            Check that all decisions are approved
            prior to changing Referral Status
        """
        return self.decision_set.filter(verdict='Approved').count() == 3

    def decisions_created(self):
        """
            Check that only 3 decisions are associated
            with any one Referral.
        """
        return self.decision_count == 3

    def screens_rejected(self):
        # TODO: check if it needs to be all three or single rejection
        raise(NotImplementedError)

    @transition(field=status, source='*', target=STATUS_APPROVED, conditions=[all_decisions_approved])
    def approve(self):
        """
            Add Client to Phase when Referral approved
        """
        # p = Phase(phase_id='Phase One')
        # p.save()
        # self.client.phase = p
        # import pdb; pdb.set_trace()
        if self.client.status != IntakeStatus.STATUS_ACCEPTED:
            self.client.status = IntakeStatus.STATUS_ACCEPTED
            self.client.save()


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

    made_by = models.CharField(max_length=20, choices=ROLES, null=True)
    date_received = models.DateField(null=True, blank=True)
    date_completed = models.DateField(null=True, blank=True)
    verdict = models.CharField('Verdict', choices=STATUS_CHOICES,
                               max_length=20, default=STATUS_PENDING)
    referral = models.ForeignKey(
        'intake.Referral', on_delete=models.CASCADE)

    # Efficient way to look up foreign keys
    # Entry.objects.select_related('blog').get(id=5)
    # This Returns objects not foreign key. Can you just pass referral?

    def get_absolute_url(self):
        return reverse('intake:referral-detail', kwargs={'pk': self.referral.id})

    def __str__(self):
        return f"{self.made_by} Decision for {self.referral.client}"

    class Meta:

        permissions = [('can_decide', 'Can Decide')]
