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
    created_date = models.DateTimeField(default=date.today)

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


class Referrals(ConcurrentTransitionMixin, models.Model):

    # TODO: Refactor out all this enums to Dataclass
    STATUS_PENDING_ASSESS = 'Pending Assessment'
    STATUS_PENDING_ACCEPT = 'Pending Client Acceptance'
    STATUS_PENDING_TERMINATION = 'Pending Termination'
    STATUS_PENDING = 'Pending'

    STATUS_REJECTED = 'Rejected'
    STATUS_ACTIVE = 'Active'
    STATUS_TERMINATED = 'Terminated'
    STATUS_DECLINED = 'Declined'
    STATUS_REJECTED = 'Rejected'
    STATUS_GRADUATED = 'Graduated'
    STATUS_AWOL = 'AWOL'
    STATUS_MEDICALLEAVE = 'Medical Leave'
    STATUS_IN_CUSTODY = 'In Custody'
    # STATUS_NULL = None

    STATUS_CHOICES = (
        (STATUS_PENDING, STATUS_PENDING),
        (STATUS_PENDING_ASSESS, STATUS_PENDING_ASSESS),
        (STATUS_PENDING_ACCEPT, STATUS_PENDING_ACCEPT),
        (STATUS_REJECTED, STATUS_REJECTED),
        (STATUS_ACTIVE, STATUS_ACTIVE),
        (STATUS_TERMINATED, STATUS_TERMINATED),
        (STATUS_GRADUATED, STATUS_GRADUATED),
        (STATUS_AWOL, STATUS_AWOL),
        (STATUS_TERMINATED, STATUS_TERMINATED),
        (STATUS_MEDICALLEAVE, STATUS_MEDICALLEAVE),
        (STATUS_DECLINED, STATUS_DECLINED),
        (STATUS_REJECTED, STATUS_REJECTED),
        (STATUS_IN_CUSTODY, STATUS_IN_CUSTODY),
        (STATUS_PENDING_TERMINATION, STATUS_PENDING_TERMINATION),
        # (STATUS_NULL, STATUS_NULL)
    )

    TRACKS_CHOICES = (1, 2, 3, 4)

# Reject Reasons
    REJECT_NULL = None
    REJECT_PRIOR = 'Prior violations'
    REJECT_INELIGIBLE = 'ineligible'
    REJECT_DEFENDANT = 'defendant'
    REJECT_NO_SHOW = 'did not appear'
    REJECT_OTHER = 'other'

    REJECT_REASON_CHOICES = (
        (REJECT_NULL, REJECT_NULL),
        (REJECT_PRIOR, REJECT_PRIOR),
        (REJECT_INELIGIBLE, REJECT_INELIGIBLE),
        (REJECT_DEFENDANT, REJECT_DEFENDANT),
        (REJECT_NO_SHOW, REJECT_NO_SHOW),
        (REJECT_OTHER, REJECT_OTHER),
    )

    DECISION_APPROVED = 'Approved'
    DECISION_REJECTED = 'Rejected'

    DECISION_CHOICES = (
        (DECISION_APPROVED, DECISION_APPROVED),
        (DECISION_REJECTED, DECISION_REJECTED)
    )

    CLIENT_ACCEPTED = 'Client Accepted'
    CLIENT_REJECTED = 'Client Rejected'

    CLIENT_DECISION = ((CLIENT_ACCEPTED, CLIENT_ACCEPTED),
                       (CLIENT_REJECTED, CLIENT_REJECTED))

    refid = models.AutoField(db_column='RefID', primary_key=True)

    clientid = models.CharField(
        db_column='ClientID', unique=True, max_length=15)

    casenums = models.CharField(
        db_column='CaseNums', max_length=255, blank=True, null=True)

    charges = models.CharField(
        db_column='Charges', max_length=100, blank=True, null=True)

    spn = models.CharField(db_column='SPN', max_length=8,
                           blank=True, null=True)

    stateid = models.CharField(
        db_column='StateID', max_length=15, blank=True, null=True)

    lastname = models.CharField(
        db_column='LastName', max_length=20, blank=True, null=True)

    firstname = models.CharField(
        db_column='FirstName', max_length=20, blank=True, null=True)

    middlename = models.CharField(
        db_column='MiddleName', max_length=20, blank=True, null=True)

    ssn = models.CharField(
        db_column='SSN', max_length=11, blank=True, null=True)

    track = models.CharField(db_column='Track', max_length=1)

    enrolldate = models.DateField(
        db_column='EnrollDate', blank=True, null=True)

    rejectreason = models.CharField(
        db_column='RejectReason', max_length=50, blank=True, null=True)

    dob = models.DateField(db_column='DOB', blank=True, null=True)

    race = models.CharField(
        db_column='Race', max_length=35, blank=True, null=True)

    sex = models.CharField(db_column='Sex', choices=(('M', 'Male'), ('F', 'Female')), max_length=1,
                           blank=True, null=True)
    # Changed to FSM field

    status = FSMField(db_column='Status', choices=STATUS_CHOICES,
                      max_length=50)

    division = models.IntegerField(db_column='Division', blank=True, null=True)

    location = models.CharField(
        db_column='Location', max_length=10, blank=True, null=True)

    cell = models.CharField(
        db_column='Cell', max_length=10, blank=True, null=True)

    referredby = models.CharField(
        db_column='ReferredBy', max_length=50, blank=True, null=True)

    referreddate = models.DateField(
        db_column='ReferredDate', blank=True, null=True)

    pretrialname = models.CharField(
        db_column='PretrialName', max_length=50, blank=True, null=True)

    pretrialreceived = models.DateField(
        db_column='PretrialReceived', blank=True, null=True)

    pretrialcompleted = models.DateField(
        db_column='PretrialCompleted', blank=True, null=True)

    pretrialdecision = models.CharField(
        db_column='PretrialDecision', choices=DECISION_CHOICES, max_length=10, blank=True, null=True)

    defensename = models.CharField(
        db_column='DefenseName', max_length=50, blank=True, null=True)

    defensereceived = models.DateField(
        db_column='DefenseReceived', blank=True, null=True)

    defensecompleted = models.DateField(
        db_column='DefenseCompleted', blank=True, null=True)

    defensedecision = models.CharField(
        db_column='DefenseDecision', choices=DECISION_CHOICES, max_length=10, blank=True, null=True)

    daname = models.CharField(
        db_column='DAName', max_length=50, blank=True, null=True)

    dareceived = models.DateField(
        db_column='DAReceived', blank=True, null=True)

    dacompleted = models.DateField(
        db_column='DACompleted', blank=True, null=True)

    dadecision = models.CharField(
        db_column='DADecision', choices=DECISION_CHOICES, max_length=10, blank=True, null=True)

    assessname = models.CharField(
        db_column='AssessName', max_length=50, blank=True, null=True)

    assessreceived = models.DateField(
        db_column='AssessReceived', blank=True, null=True)

    assesscompleted = models.DateField(
        db_column='AssessCompleted', blank=True, null=True)

    teamreceived = models.DateField(
        db_column='TeamReceived', blank=True, null=True)

    teamcompleted = models.DateField(
        db_column='TeamCompleted', blank=True, null=True)

    teamdecision = models.CharField(
        db_column='TeamDecision', choices=DECISION_CHOICES, max_length=10, blank=True, null=True)

    arrests = models.IntegerField(db_column='Arrests', blank=True, null=True)

    felonies = models.IntegerField(db_column='Felonies', blank=True, null=True)

    misdemeanors = models.IntegerField(
        db_column='Misdemeanors', blank=True, null=True)

    firstarrestyear = models.IntegerField(
        db_column='FirstArrestYear', blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=50, blank=True, null=True)

    accepteddate = models.DateField(
        db_column='AcceptedDate', blank=True, null=True)

    county = models.CharField(
        db_column='County', max_length=50, blank=True, null=True)

    type = models.CharField(
        db_column='Type', max_length=25, blank=True, null=True)

    termreason = models.CharField(
        db_column='TermReason', max_length=25, blank=True, null=True)

    def create_clientid(self):
        # TODO: add algorithm to create
        pre_text = date.today().year
        try:
            latest_id = int(Referrals.objects.latest('clientid').clientid)
            new_id = latest_id + 1
        except Referrals.DoesNotExist:
            new_id = f'{pre_text}000{1}'

        return new_id

    def __init__(self, *args, **kwargs):
        super(Referrals, self).__init__(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'Referrals'
        app_label = 'cases'
        verbose_name_plural = 'referrals'

# Conditions
# TODO: use post save signal to check decisions
    def reviews_approve(self):
        return self.dadecision == self.DECISION_APPROVED and self.defensedecision == self.DECISION_APPROVED and self.pretrialdecision == self.DECISION_APPROVED

    def reviews_reject(self):
        # unnecessary condition
        return self.dadecision != self.DECISION_APPROVED or self.defensedecision != self.DECISION_APPROVED or self.pretrialdecision != self.DECISION_APPROVED

    def assess_approve(self):
        # TODO: this will need a decision field
        return self.assesscompleted

    def assess_reject(self):
        return not self.assesscompleted

    def client_accepted(self):
        return self.accepteddate

    def client_declined(self):
        return not self.accepteddate

# Transitions
    # TODO: add permissions for users
    # TODO: put source back to STATUS_NULL - causing sql.IntegrityError
    @transition(field=status, source='*', target=STATUS_PENDING)
    def add_referral(self):
         # TODO: send notifications/ add to logs
        pass

    # TODO: link this to button in form
    @transition(field=status, source=STATUS_PENDING, target=STATUS_PENDING_ASSESS, conditions=[reviews_approve], on_error=STATUS_PENDING)
    def approve_referral(self):
        # TODO: side effect -> send notification for assessment
        # status changed when this is called, but not saved
        pass

    @transition(field=status, source=STATUS_PENDING, target=STATUS_PENDING_TERMINATION, conditions=[reviews_reject], on_error=STATUS_PENDING)
    def reject_referral(self):
        pass

    @transition(field=status, source=STATUS_PENDING_ASSESS, target=STATUS_PENDING_ACCEPT, conditions=[assess_approve], on_error=STATUS_PENDING_ASSESS)
    def assess_referral(self):
        # TODO: side effect ->
        pass

    @transition(field=status, source=STATUS_PENDING_ASSESS, target=STATUS_REJECTED, conditions=[assess_reject], on_error=STATUS_PENDING_ASSESS)
    def reject_assess_referral(self):
        # TODO: side effect ->
        pass

    @transition(field=status, source=STATUS_PENDING_ACCEPT, target=CLIENT_ACCEPTED, on_error=STATUS_PENDING_ASSESS)
    def client_accept(self):
        # TODO: side effect ->
        # Add phase
        # Get Created Date
        pass

    @transition(field=status, source=STATUS_PENDING_ACCEPT, target=CLIENT_REJECTED, on_error=STATUS_PENDING_ACCEPT)
    def client_decline(self):
        # TODO: side effect ->
        pass

    @transition(field=status, source=CLIENT_ACCEPTED, target=STATUS_ACTIVE)
    def activate_client(self):
        # error message for activate - when called in view
        # print('Client Activated')
        pass

    def __str__(self):
        return f'Referral {self.refid}'

    def clean(self):
        if not self.reviews_approve() and self.status == self.STATUS_PENDING_ASSESS:
            self.add_referral()
        # TODO: need to check assesment state 7/11
        elif self.reviews_approve() and self.status == self.STATUS_PENDING:
            self.approve_referral()

        return super().clean()

    def get_absolute_url(self):
        return reverse('referrals-update', kwargs={'pk': self.refid})


class Clients(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

# TODO: make foreign key to Referrals table
    clientid = models.CharField(
        db_column='ClientID', unique=True, max_length=15)

    startdate = models.DateField(db_column='StartDate', blank=True, null=True)

    dischargedate = models.DateField(
        db_column='DischargeDate', blank=True, null=True)

    cellphone = models.CharField(
        db_column='CellPhone', max_length=50, blank=True, null=True)

    email = models.EmailField(
        db_column='Email', max_length=75, blank=True, null=True)

    message = models.CharField(
        db_column='Message', max_length=50, blank=True, null=True)

    messagesource = models.CharField(
        db_column='MessageSource', max_length=50, blank=True, null=True)

    yearlyincome = models.CharField(
        db_column='YearlyIncome', max_length=20, blank=True, null=True)

    incomesource = models.CharField(
        db_column='IncomeSource', max_length=25, blank=True, null=True)

    educationyrs = models.IntegerField(
        db_column='EducationYrs', blank=True, null=True)

    educationlevel = models.CharField(
        db_column='EducationLevel', max_length=50, blank=True, null=True)

    highschoolgrad = models.CharField(
        db_column='HighSchoolGrad', max_length=3, blank=True, null=True)

    ged = models.CharField(db_column='GED', max_length=3,
                           blank=True, null=True)

    militaryservice = models.BooleanField(db_column='MilitaryService')

    vaeligible = models.BooleanField(db_column='VAEligible')

    maritalstatus = models.CharField(
        db_column='MaritalStatus', max_length=20, blank=True, null=True)

    pregnant = models.CharField(
        db_column='Pregnant', max_length=5, blank=True, null=True)

    children = models.CharField(
        db_column='Children', max_length=12, blank=True, null=True)

    childnarrative = models.TextField(
        db_column='ChildNarrative', blank=True, null=True)

    diagnosis = models.TextField(db_column='Diagnosis', blank=True, null=True)

    suicide = models.BooleanField(db_column='Suicide')

    violence = models.BooleanField(db_column='Violence')

    health = models.TextField(db_column='Health', blank=True, null=True)

    ghmedications = models.TextField(
        db_column='GhMedications', blank=True, null=True)

    prenatal = models.TextField(db_column='Prenatal', blank=True, null=True)

    tbstatus = models.CharField(
        db_column='TBStatus', max_length=50, blank=True, null=True)

    physicalabuse = models.BooleanField(db_column='PhysicalAbuse')

    sexualabuse = models.BooleanField(db_column='SexualAbuse')

    insurance = models.CharField(
        db_column='Insurance', max_length=50, blank=True, null=True)

    primarydrug = models.CharField(
        db_column='PrimaryDrug', max_length=50, blank=True, null=True)

    substanceuse = models.CharField(
        db_column='SubstanceUse', max_length=6, blank=True, null=True)

    sobriety = models.CharField(
        db_column='Sobriety', max_length=50, blank=True, null=True)

    needleuse = models.BooleanField(db_column='NeedleUse')

    addictionseverityindex = models.CharField(
        db_column='AddictionSeverityIndex', max_length=50, blank=True, null=True)

    familyoforiginyn = models.BooleanField(db_column='FamilyofOriginYN')

    familyoforiginuse = models.CharField(
        db_column='FamilyofOriginUse', max_length=250, blank=True, null=True)

    spouseuseyn = models.BooleanField(db_column='SpouseUseYN')

    spouseuse = models.CharField(
        db_column='SpouseUse', max_length=250, blank=True, null=True)

    testtype = models.CharField(
        db_column='TestType', max_length=50, blank=True, null=True)

    testresults = models.CharField(
        db_column='TestResults', max_length=250, blank=True, null=True)

    employedatgraduation = models.BooleanField(
        db_column='EmployedAtGraduation', blank=True, null=True)

    outcomecomments = models.TextField(
        db_column='OutcomeComments', blank=True, null=True)

    cmuserid = models.CharField(
        db_column='CMUserID', max_length=50, blank=True, null=True)

    couserid = models.CharField(
        db_column='COUserID', max_length=50, blank=True, null=True)

    phase = models.CharField(
        db_column='Phase', max_length=1, blank=True, null=True)

    stopbilling = models.BooleanField(
        db_column='StopBilling', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=50, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    lastpositive = models.DateField(
        db_column='LastPositive', blank=True, null=True)

    lep = models.IntegerField(db_column='LEP', blank=True, null=True)

    employedatstart = models.CharField(
        db_column='EmployedAtStart', max_length=12, blank=True, null=True)

    employedatgrad = models.CharField(
        db_column='EmployedAtGrad', max_length=12, blank=True, null=True)

    asam_loc = models.DecimalField(
        db_column='ASAM_LOC', max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Clients'
        verbose_name_plural = 'clients'


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
