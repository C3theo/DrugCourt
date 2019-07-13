# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from django_fsm import FSMField, transition, ConcurrentTransitionMixin, TransitionNotAllowed
from django.urls import reverse
from datetime import datetime, date
from django.db.models import F




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


class Appinfo(models.Model):

    orgname = models.CharField(
        db_column='OrgName', primary_key=True, max_length=50)

    apppath = models.CharField(
        db_column='AppPath', max_length=75, blank=True, null=True)

    photopath = models.CharField(
        db_column='PhotoPath', max_length=75, blank=True, null=True)

    track = models.CharField(
        db_column='Track', max_length=1, blank=True, null=True)

    site = models.CharField(
        db_column='Site', max_length=40, blank=True, null=True)

    datastart = models.DateTimeField(
        db_column='DataStart', blank=True, null=True)

    type = models.CharField(
        db_column='Type', max_length=50, blank=True, null=True)

    judge = models.CharField(
        db_column='Judge', max_length=50, blank=True, null=True)

    coordinator = models.CharField(
        db_column='Coordinator', max_length=50, blank=True, null=True)

    docpath = models.CharField(
        db_column='DocPath', max_length=125, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AppInfo'


class Approles(models.Model):

    roleid = models.AutoField(db_column='RoleID', primary_key=True)

    roletitle = models.CharField(
        db_column='RoleTitle', max_length=30, blank=True, null=True)

    disciplineid = models.IntegerField(
        db_column='DisciplineID', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AppRoles'


class Assessments(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    assessdate = models.DateField(
        db_column='AssessDate', blank=True, null=True)

    assessscore = models.IntegerField(
        db_column='AssessScore', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=15, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    assesstool = models.CharField(
        db_column='AssessTool', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Assessments'


class Attorneys(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    attorneyname = models.CharField(db_column='AttorneyName', max_length=55)

    attorneytype = models.CharField(
        db_column='AttorneyType', max_length=50, blank=True, null=True)

    email = models.CharField(
        db_column='Email', max_length=75, blank=True, null=True)

    phone = models.CharField(
        db_column='Phone', max_length=12, blank=True, null=True)

    active = models.BooleanField(db_column='Active', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Attorneys'


class Cs(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    csdate = models.DateTimeField(db_column='CSDate')

    csassignment = models.CharField(
        db_column='CSAssignment', max_length=50, blank=True, null=True)

    cshours = models.SmallIntegerField(db_column='CSHours')

    csverifiedby = models.CharField(
        db_column='CSVerifiedBy', max_length=50, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CS'


class Casenums(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    casenum = models.CharField(db_column='CaseNum', max_length=11)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    charges = models.CharField(
        db_column='Charges', max_length=255, blank=True, null=True)

    arrestdate = models.DateTimeField(
        db_column='ArrestDate', blank=True, null=True)

    dispositiondate = models.DateTimeField(
        db_column='DispositionDate', blank=True, null=True)

    disposition = models.CharField(
        db_column='Disposition', max_length=200, blank=True, null=True)

    division = models.IntegerField(db_column='Division', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=15, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CaseNums'


class Children(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    childgender = models.CharField(db_column='ChildGender', max_length=50)

    name = models.CharField(
        db_column='Name', max_length=50, blank=True, null=True)

    childdob = models.DateTimeField(
        db_column='ChildDOB', blank=True, null=True)

    age = models.CharField(db_column='Age', max_length=8,
                           blank=True, null=True)

    contact = models.CharField(
        db_column='Contact', max_length=50, blank=True, null=True)

    custody = models.CharField(
        db_column='Custody', max_length=50, blank=True, null=True)

    cpscase = models.CharField(
        db_column='CPSCase', max_length=50, blank=True, null=True)

    home = models.CharField(
        db_column='Home', max_length=50, blank=True, null=True)

    otherhome = models.CharField(
        db_column='OtherHome', max_length=50, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Children'


class Chroniccond(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    condition = models.CharField(
        db_column='Condition', max_length=100, blank=True, null=True)

    diagnosis = models.TextField(db_column='Diagnosis', blank=True, null=True)

    physician = models.CharField(
        db_column='Physician', max_length=50, blank=True, null=True)

    userid = models.CharField(
        db_column='userID', max_length=10, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = True
        db_table = 'ChronicCond'


class Clientaddress(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    activedate = models.DateTimeField(db_column='Activedate')

    residencetype = models.CharField(db_column='ResidenceType', max_length=25)

    address1 = models.CharField(
        db_column='Address1', max_length=75, blank=True, null=True)

    address2 = models.CharField(
        db_column='Address2', max_length=75, blank=True, null=True)

    city = models.CharField(
        db_column='City', max_length=25, blank=True, null=True)

    state = models.CharField(
        db_column='State', max_length=3, blank=True, null=True)

    zip = models.CharField(
        db_column='Zip', max_length=10, blank=True, null=True)

    homephone = models.CharField(
        db_column='HomePhone', max_length=14, blank=True, null=True)

    contact = models.CharField(
        db_column='Contact', max_length=20, blank=True, null=True)
    payment = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ClientAddress'


class Clientcontacts(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    clientrelationship = models.CharField(
        db_column='ClientRelationship', max_length=20)

    contactname = models.CharField(db_column='ContactName', max_length=20)

    contactphone1 = models.CharField(
        db_column='ContactPhone1', max_length=12, blank=True, null=True)

    contactphone2 = models.CharField(
        db_column='ContactPhone2', max_length=10, blank=True, null=True)

    contactaddress = models.CharField(
        db_column='ContactAddress', max_length=255, blank=True, null=True)

    contactcitystatezip = models.CharField(
        db_column='ContactCityStateZip', max_length=50, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ClientContacts'


class Clientdocs(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    doctype = models.CharField(db_column='DocType', max_length=25)

    userid = models.CharField(
        db_column='UserID', max_length=50, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    docname = models.CharField(
        db_column='DocName', max_length=100, blank=True, null=True)

    docdate = models.DateField(db_column='DocDate', blank=True, null=True)

    doclink = models.CharField(
        db_column='DocLink', max_length=150, blank=True, null=True)

    docnote = models.CharField(
        db_column='DocNote', max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ClientDocs'


class Clientlog(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    changedate = models.DateTimeField(db_column='ChangeDate')

    changefield = models.CharField(db_column='ChangeField', max_length=255)

    changeinfo = models.CharField(db_column='ChangeInfo', max_length=255)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ClientLog'


class Clientphase(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    phase = models.CharField(db_column='Phase', max_length=1)

    phasestart = models.DateTimeField(db_column='PhaseStart')

    phaseend = models.DateTimeField(
        db_column='PhaseEnd', blank=True, null=True)
    completed = models.BooleanField(blank=True, null=True)

    totaldays = models.IntegerField(
        db_column='TotalDays', blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = True
        db_table = 'ClientPhase'



class Court(models.Model):

    courtid = models.AutoField(db_column='CourtID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    courtdate = models.DateTimeField(db_column='CourtDate')

    event = models.CharField(
        db_column='Event', max_length=50, blank=True, null=True)

    courtdatetype = models.CharField(
        db_column='CourtDateType', max_length=10, blank=True, null=True)

    phase = models.CharField(
        db_column='Phase', max_length=1, blank=True, null=True)

    attendance = models.CharField(
        db_column='Attendance', max_length=50, blank=True, null=True)

    comments = models.TextField(db_column='Comments', blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=15, blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = True
        db_table = 'Court'


class Crimhistory(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    charge = models.CharField(
        db_column='Charge', max_length=50, blank=True, null=True)

    chargetype = models.CharField(
        db_column='ChargeType', max_length=15, blank=True, null=True)

    penalcode = models.CharField(
        db_column='PenalCode', max_length=30, blank=True, null=True)

    status = models.CharField(
        db_column='Status', max_length=50, blank=True, null=True)

    chargedate = models.DateTimeField(
        db_column='ChargeDate', blank=True, null=True)

    chargenote = models.CharField(
        db_column='ChargeNote', max_length=150, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CrimHistory'


class Dblog(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    logdate = models.DateField(db_column='LogDate', blank=True, null=True)

    track = models.CharField(
        db_column='Track', max_length=1, blank=True, null=True)

    cntpending = models.IntegerField(
        db_column='CntPending', blank=True, null=True)

    cntactive = models.IntegerField(
        db_column='CntActive', blank=True, null=True)

    cntawol = models.IntegerField(db_column='CntAWOL', blank=True, null=True)

    cntpendingterm = models.IntegerField(
        db_column='CntPendingTerm', blank=True, null=True)

    cntincustody = models.IntegerField(
        db_column='CntInCustody', blank=True, null=True)

    cntmedicalleave = models.IntegerField(
        db_column='CntMedicalLeave', blank=True, null=True)

    cntpositivescreens = models.IntegerField(
        db_column='CntPositiveScreens', blank=True, null=True)

    cntoverinphase = models.IntegerField(
        db_column='CntOverInPhase', blank=True, null=True)

    cntphalert = models.IntegerField(
        db_column='CntPhAlert', blank=True, null=True)

    cntfeesalert = models.IntegerField(
        db_column='CntFeesAlert', blank=True, null=True)

    cntstepup = models.IntegerField(
        db_column='CntStepUp', blank=True, null=True)

    cntproposals = models.IntegerField(
        db_column='CntProposals', blank=True, null=True)

    cnt12step = models.IntegerField(
        db_column='Cnt12Step', blank=True, null=True)

    cntnrd = models.IntegerField(db_column='CntNRD', blank=True, null=True)

    cntsessions = models.IntegerField(
        db_column='CntSessions', blank=True, null=True)

    cntobjectivesdue = models.IntegerField(
        db_column='CntObjectivesDue', blank=True, null=True)

    cntratingsdue = models.IntegerField(
        db_column='CntRatingsDue', blank=True, null=True)

    cntnotesdue = models.IntegerField(
        db_column='CntNotesDue', blank=True, null=True)

    cntcourtdates = models.IntegerField(
        db_column='CntCourtDates', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'DBLog'


class Dashboard(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    cntdate = models.DateTimeField(db_column='CntDate', blank=True, null=True)

    track = models.CharField(
        db_column='Track', max_length=1, blank=True, null=True)

    site = models.CharField(db_column='Site', max_length=40)

    cntpending = models.IntegerField(
        db_column='CntPending', blank=True, null=True)

    cntactive = models.IntegerField(
        db_column='CntActive', blank=True, null=True)

    cntawol = models.IntegerField(db_column='CntAWOL', blank=True, null=True)

    cntpendingterm = models.IntegerField(
        db_column='CntPendingTerm', blank=True, null=True)

    cntincustody = models.IntegerField(
        db_column='CntInCustody', blank=True, null=True)

    cntmedicalleave = models.IntegerField(
        db_column='CntMedicalLeave', blank=True, null=True)

    cntpositivescreens = models.IntegerField(
        db_column='CntPositiveScreens', blank=True, null=True)

    cntoverinphase = models.IntegerField(
        db_column='CntOverInPhase', blank=True, null=True)

    cntphalert = models.IntegerField(
        db_column='CntPhAlert', blank=True, null=True)

    cntfeesalert = models.IntegerField(
        db_column='CntFeesAlert', blank=True, null=True)

    cntstepup = models.IntegerField(
        db_column='CntStepUp', blank=True, null=True)

    cntproposals = models.IntegerField(
        db_column='CntProposals', blank=True, null=True)

    cnt12step = models.IntegerField(
        db_column='Cnt12Step', blank=True, null=True)

    cntnrd = models.IntegerField(db_column='CntNRD', blank=True, null=True)

    cntsessions = models.IntegerField(
        db_column='CntSessions', blank=True, null=True)

    cntobjectivesdue = models.IntegerField(
        db_column='CntObjectivesDue', blank=True, null=True)

    cntratingsdue = models.IntegerField(
        db_column='CntRatingsDue', blank=True, null=True)

    cntnotesdue = models.IntegerField(
        db_column='CntNotesDue', blank=True, null=True)

    cntcourtdates = models.IntegerField(
        db_column='CntCourtDates', blank=True, null=True)

    cntbilling = models.IntegerField(
        db_column='CntBilling', blank=True, null=True)

    cntpayments = models.IntegerField(
        db_column='CntPayments', blank=True, null=True)

    cnttxattendance = models.IntegerField(
        db_column='CntTxAttendance', blank=True, null=True)

    cntscreens = models.IntegerField(
        db_column='CntScreens', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Dashboard'


class Debttype(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    debttype = models.CharField(
        db_column='DebtType', max_length=15, blank=True, null=True)

    sort = models.CharField(
        db_column='Sort', max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'DebtType'


class Debts(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    debttype = models.CharField(
        db_column='DebtType', max_length=15, blank=True, null=True)

    debtdate = models.DateTimeField(
        db_column='DebtDate', blank=True, null=True)

    debtamount = models.DecimalField(
        db_column='DebtAmount', max_digits=19, decimal_places=4, blank=True, null=True)

    debtbalance = models.DecimalField(
        db_column='DebtBalance', max_digits=19, decimal_places=4, blank=True, null=True)

    statuscode = models.CharField(
        db_column='StatusCode', max_length=15, blank=True, null=True)

    comment = models.TextField(db_column='Comment', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=20, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = True
        db_table = 'Debts'


class Demographics(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    createdate = models.DateField(
        db_column='CreateDate', blank=True, null=True)

    white_m = models.IntegerField(db_column='White_M', blank=True, null=True)

    white_f = models.IntegerField(db_column='White_F', blank=True, null=True)

    white_t = models.IntegerField(db_column='White_T', blank=True, null=True)

    amindianalaskan_m = models.IntegerField(
        db_column='AmIndianAlaskan_M', blank=True, null=True)

    amindianalaskan_f = models.IntegerField(
        db_column='AmIndianAlaskan_F', blank=True, null=True)

    amindianalaskan_t = models.IntegerField(
        db_column='AmIndianAlaskan_T', blank=True, null=True)

    asian_m = models.IntegerField(db_column='Asian_M', blank=True, null=True)

    asian_f = models.IntegerField(db_column='Asian_F', blank=True, null=True)

    asian_t = models.IntegerField(db_column='Asian_T', blank=True, null=True)

    black_m = models.IntegerField(db_column='Black_M', blank=True, null=True)

    black_f = models.IntegerField(db_column='Black_F', blank=True, null=True)

    black_t = models.IntegerField(db_column='Black_T', blank=True, null=True)

    hispanic_m = models.IntegerField(
        db_column='Hispanic_M', blank=True, null=True)

    hispanic_f = models.IntegerField(
        db_column='Hispanic_F', blank=True, null=True)

    hispanic_t = models.IntegerField(
        db_column='Hispanic_T', blank=True, null=True)

    mideast_m = models.IntegerField(
        db_column='MidEast_M', blank=True, null=True)

    mideast_f = models.IntegerField(
        db_column='MidEast_F', blank=True, null=True)

    mideast_t = models.IntegerField(
        db_column='MidEast_T', blank=True, null=True)

    hawaiian_m = models.IntegerField(
        db_column='Hawaiian_M', blank=True, null=True)

    hawaiian_f = models.IntegerField(
        db_column='Hawaiian_F', blank=True, null=True)

    hawaiian_t = models.IntegerField(
        db_column='Hawaiian_T', blank=True, null=True)

    other_m = models.IntegerField(db_column='Other_M', blank=True, null=True)

    other_f = models.IntegerField(db_column='Other_F', blank=True, null=True)

    other_t = models.IntegerField(db_column='Other_T', blank=True, null=True)

    twoormore_m = models.IntegerField(
        db_column='TwoOrMore_M', blank=True, null=True)

    twoormore_f = models.IntegerField(
        db_column='TwoOrMore_F', blank=True, null=True)

    twoormore_t = models.IntegerField(
        db_column='TwoOrMore_T', blank=True, null=True)

    elementary = models.IntegerField(
        db_column='Elementary', blank=True, null=True)

    middleschool = models.IntegerField(
        db_column='MiddleSchool', blank=True, null=True)

    somehighschool = models.IntegerField(
        db_column='SomeHighSchool', blank=True, null=True)

    highschoolged = models.IntegerField(
        db_column='HighSchoolGED', blank=True, null=True)

    somecollege = models.IntegerField(
        db_column='SomeCollege', blank=True, null=True)

    associate = models.IntegerField(
        db_column='Associate', blank=True, null=True)

    bachelor = models.IntegerField(db_column='Bachelor', blank=True, null=True)

    graduate = models.IntegerField(db_column='Graduate', blank=True, null=True)

    lep = models.IntegerField(db_column='LEP', blank=True, null=True)
    # # Field renamed because it wasn't a valid Python identifier.
    number_11andunder_m = models.IntegerField(
        db_column='11andUnder_M', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_11andunder_f = models.IntegerField(
        db_column='11andUnder_F', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_11andunder_t = models.IntegerField(
        db_column='11andUnder_T', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_12to17_m = models.IntegerField(
        db_column='12to17_M', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_12to17_f = models.IntegerField(
        db_column='12to17_F', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_12to17_t = models.IntegerField(
        db_column='12to17_T', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_18to20_m = models.IntegerField(
        db_column='18to20_M', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_18to20_f = models.IntegerField(
        db_column='18to20_F', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_18to20_t = models.IntegerField(
        db_column='18to20_T', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_21to25_m = models.IntegerField(
        db_column='21to25_M', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_21to25_f = models.IntegerField(
        db_column='21to25_F', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_21to25_t = models.IntegerField(
        db_column='21to25_T', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_26to35_m = models.IntegerField(
        db_column='26to35_M', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_26to35_f = models.IntegerField(
        db_column='26to35_F', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_26to35_t = models.IntegerField(
        db_column='26to35_T', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_36to45_m = models.IntegerField(
        db_column='36to45_M', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_36to45_f = models.IntegerField(
        db_column='36to45_F', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_36to45_t = models.IntegerField(
        db_column='36to45_T', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_46to55_m = models.IntegerField(
        db_column='46to55_M', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_46to55_f = models.IntegerField(
        db_column='46to55_F', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_46to55_t = models.IntegerField(
        db_column='46to55_T', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_56to65_m = models.IntegerField(
        db_column='56to65_M', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_56to65_f = models.IntegerField(
        db_column='56to65_F', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_56to65_t = models.IntegerField(
        db_column='56to65_T', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_66orolder_m = models.IntegerField(
        db_column='66orOlder_M', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_66orolder_f = models.IntegerField(
        db_column='66orOlder_F', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_66orolder_t = models.IntegerField(
        db_column='66orOlder_T', blank=True, null=True)

    gradunandem = models.IntegerField(
        db_column='GradUnandEm', blank=True, null=True)

    gradunandun = models.IntegerField(
        db_column='GradUnandUn', blank=True, null=True)

    grademandun = models.IntegerField(
        db_column='GradEmandUn', blank=True, null=True)

    grademandem = models.IntegerField(
        db_column='GradEmandEm', blank=True, null=True)

    married = models.IntegerField(db_column='Married', blank=True, null=True)

    commonlaw = models.IntegerField(
        db_column='CommonLaw', blank=True, null=True)

    separated = models.IntegerField(
        db_column='Separated', blank=True, null=True)

    divorced = models.IntegerField(db_column='Divorced', blank=True, null=True)

    widowed = models.IntegerField(db_column='Widowed', blank=True, null=True)

    single = models.IntegerField(db_column='Single', blank=True, null=True)

    noincome = models.IntegerField(db_column='NoIncome', blank=True, null=True)

    under999 = models.IntegerField(db_column='Under999', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_1kto4999 = models.IntegerField(
        db_column='1Kto4999', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_5kto9999 = models.IntegerField(
        db_column='5Kto9999', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_15kto19999 = models.IntegerField(
        db_column='15Kto19999', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_20kto34999 = models.IntegerField(
        db_column='20Kto34999', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_35kto44999 = models.IntegerField(
        db_column='35Kto44999', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_45kto54999 = models.IntegerField(
        db_column='45Kto54999', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_55kto64999 = models.IntegerField(
        db_column='55Kto64999', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_65kto74999 = models.IntegerField(
        db_column='65Kto74999', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_75korhigher = models.IntegerField(
        db_column='75KorHigher', blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    datastart = models.DateTimeField(
        db_column='DataStart', blank=True, null=True)

    dataend = models.DateTimeField(db_column='DataEnd', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_10kto14999 = models.IntegerField(
        db_column='10Kto14999', blank=True, null=True)

    totalactive = models.IntegerField(
        db_column='TotalActive', blank=True, null=True)

    totalgrads = models.IntegerField(
        db_column='TotalGrads', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Demographics'


class Disciplines(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    discipline = models.CharField(
        db_column='Discipline', max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Disciplines'


class Drugtypes(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    drugtype = models.CharField(db_column='DrugType', max_length=50)

    class Meta:
        managed = True
        db_table = 'DrugTypes'


class Educationlevel(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    level = models.CharField(db_column='Level', max_length=50)

    class Meta:
        managed = True
        db_table = 'EducationLevel'


class Employment(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    occupation = models.CharField(
        db_column='Occupation', max_length=50, blank=True, null=True)

    employer = models.CharField(db_column='Employer', max_length=50)

    contact = models.CharField(
        db_column='Contact', max_length=25, blank=True, null=True)

    address = models.CharField(
        db_column='Address', max_length=50, blank=True, null=True)

    city = models.CharField(
        db_column='City', max_length=25, blank=True, null=True)

    state = models.CharField(
        db_column='State', max_length=2, blank=True, null=True)

    zip = models.CharField(
        db_column='Zip', max_length=10, blank=True, null=True)

    phone = models.CharField(
        db_column='Phone', max_length=12, blank=True, null=True)
    doh = models.DateTimeField(db_column='DOH')

    dot = models.DateTimeField(db_column='DOT', blank=True, null=True)

    income = models.DecimalField(
        db_column='Income', max_digits=19, decimal_places=4, blank=True, null=True)

    hours = models.CharField(
        db_column='Hours', max_length=10, blank=True, null=True)

    schedule = models.CharField(
        db_column='Schedule', max_length=10, blank=True, null=True)

    payperiod = models.CharField(
        db_column='PayPeriod', max_length=10, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Employment'


class Fees(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(
        db_column='ClientID', max_length=15, blank=True, null=True)

    amount = models.DecimalField(
        db_column='Amount', max_digits=19, decimal_places=4)

    transdate = models.DateField(db_column='TransDate')

    comments = models.CharField(db_column='Comments', max_length=50)

    submitted = models.BooleanField(
        db_column='Submitted', blank=True, null=True)

    submitdate = models.DateField(
        db_column='SubmitDate', blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = True
        db_table = 'Fees'


class Frequency(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    frequency = models.CharField(
        db_column='Frequency', max_length=20, blank=True, null=True)

    sort = models.IntegerField(db_column='Sort', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Frequency'


class Gacounty(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    countyname = models.CharField(
        db_column='CountyName', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'GACounty'


class Geninfo(models.Model):

    activeparticipants = models.IntegerField(
        db_column='ActiveParticipants', blank=True, null=True)

    reviewed = models.IntegerField(db_column='Reviewed', blank=True, null=True)

    rejectedprior = models.IntegerField(
        db_column='RejectedPrior', blank=True, null=True)

    declined = models.IntegerField(db_column='Declined', blank=True, null=True)

    acceptedprepost = models.IntegerField(
        db_column='AcceptedPrePost', blank=True, null=True)

    rejected2 = models.IntegerField(
        db_column='Rejected2', blank=True, null=True)

    rejected3 = models.IntegerField(
        db_column='Rejected3', blank=True, null=True)

    rejected4 = models.IntegerField(
        db_column='Rejected4', blank=True, null=True)

    county1 = models.IntegerField(db_column='County1', blank=True, null=True)

    county2 = models.IntegerField(db_column='County2', blank=True, null=True)

    county3 = models.IntegerField(db_column='County3', blank=True, null=True)

    county4 = models.IntegerField(db_column='County4', blank=True, null=True)

    county5 = models.IntegerField(db_column='County5', blank=True, null=True)

    county6 = models.IntegerField(db_column='County6', blank=True, null=True)

    county7 = models.IntegerField(db_column='County7', blank=True, null=True)

    county8 = models.IntegerField(db_column='County8', blank=True, null=True)

    county9 = models.IntegerField(db_column='County9', blank=True, null=True)

    county10 = models.IntegerField(db_column='County10', blank=True, null=True)

    cty1name = models.CharField(
        db_column='Cty1Name', max_length=50, blank=True, null=True)

    cty2name = models.CharField(
        db_column='Cty2Name', max_length=50, blank=True, null=True)

    cty3name = models.CharField(
        db_column='Cty3Name', max_length=50, blank=True, null=True)

    cty4name = models.CharField(
        db_column='Cty4Name', max_length=50, blank=True, null=True)

    cty5name = models.CharField(
        db_column='Cty5Name', max_length=50, blank=True, null=True)

    cty6name = models.CharField(
        db_column='Cty6Name', max_length=50, blank=True, null=True)

    cty7name = models.CharField(
        db_column='Cty7Name', max_length=50, blank=True, null=True)

    cty8name = models.CharField(
        db_column='Cty8Name', max_length=50, blank=True, null=True)

    cty9name = models.CharField(
        db_column='Cty9Name', max_length=50, blank=True, null=True)

    cty10name = models.CharField(
        db_column='Cty10Name', max_length=50, blank=True, null=True)

    termadmindischarge = models.IntegerField(
        db_column='TermAdminDischarge', blank=True, null=True)

    termnoncompliance = models.IntegerField(
        db_column='TermNonCompliance', blank=True, null=True)

    termdismissed = models.IntegerField(
        db_column='TermDismissed', blank=True, null=True)

    screensbreath = models.IntegerField(
        db_column='ScreensBreath', blank=True, null=True)

    screenshair = models.IntegerField(
        db_column='ScreensHair', blank=True, null=True)

    screensurine = models.IntegerField(
        db_column='ScreensUrine', blank=True, null=True)

    screenstotal = models.IntegerField(
        db_column='ScreensTotal', blank=True, null=True)

    posscreens = models.IntegerField(
        db_column='PosScreens', blank=True, null=True)

    posscreensadmit = models.IntegerField(
        db_column='PosScreensAdmit', blank=True, null=True)

    posscreensdiluted = models.IntegerField(
        db_column='PosScreensDiluted', blank=True, null=True)

    posscreensnoshow = models.IntegerField(
        db_column='PosScreensNoShow', blank=True, null=True)

    posscreensnosample = models.IntegerField(
        db_column='PosScreensNoSample', blank=True, null=True)

    posscreensrefusal = models.IntegerField(
        db_column='PosScreensRefusal', blank=True, null=True)

    residentialtreatment = models.IntegerField(
        db_column='ResidentialTreatment', blank=True, null=True)

    substanceabusers = models.IntegerField(
        db_column='SubstanceAbusers', blank=True, null=True)

    sa_alcohol = models.IntegerField(
        db_column='SA_Alcohol', blank=True, null=True)

    sa_crack = models.IntegerField(db_column='SA_Crack', blank=True, null=True)

    sa_ecstasy = models.IntegerField(
        db_column='SA_Ecstasy', blank=True, null=True)

    sa_heroin = models.IntegerField(
        db_column='SA_Heroin', blank=True, null=True)

    sa_hallucin = models.IntegerField(
        db_column='SA_Hallucin', blank=True, null=True)

    sa_inhalants = models.IntegerField(
        db_column='SA_Inhalants', blank=True, null=True)

    sa_marijuana = models.IntegerField(
        db_column='SA_Marijuana', blank=True, null=True)

    sa_meth = models.IntegerField(db_column='SA_Meth', blank=True, null=True)

    sa_prescriptionnarc = models.IntegerField(
        db_column='SA_PrescriptionNarc', blank=True, null=True)

    sa_prescriptionother = models.IntegerField(
        db_column='SA_PrescriptionOther', blank=True, null=True)

    sa_other1 = models.IntegerField(
        db_column='SA_Other1', blank=True, null=True)

    sa_other2 = models.IntegerField(
        db_column='SA_Other2', blank=True, null=True)

    substanceusers = models.IntegerField(
        db_column='SubstanceUsers', blank=True, null=True)

    su_alcohol = models.IntegerField(
        db_column='SU_Alcohol', blank=True, null=True)

    su_crack = models.IntegerField(db_column='SU_Crack', blank=True, null=True)

    su_ecstasy = models.IntegerField(
        db_column='SU_Ecstasy', blank=True, null=True)

    su_heroin = models.IntegerField(
        db_column='SU_Heroin', blank=True, null=True)

    su_hallucin = models.IntegerField(
        db_column='SU_Hallucin', blank=True, null=True)

    su_inhalants = models.IntegerField(
        db_column='SU_Inhalants', blank=True, null=True)

    su_marijuana = models.IntegerField(
        db_column='SU_Marijuana', blank=True, null=True)

    su_meth = models.IntegerField(db_column='SU_Meth', blank=True, null=True)

    su_prescriptionnarc = models.IntegerField(
        db_column='SU_PrescriptionNarc', blank=True, null=True)

    su_prescriptionother = models.IntegerField(
        db_column='SU_PrescriptionOther', blank=True, null=True)

    su_other1 = models.IntegerField(
        db_column='SU_Other1', blank=True, null=True)

    su_other2 = models.IntegerField(
        db_column='SU_Other2', blank=True, null=True)

    asam0_5 = models.IntegerField(db_column='ASAM0_5', blank=True, null=True)

    asam1 = models.IntegerField(db_column='ASAM1', blank=True, null=True)

    asam2 = models.IntegerField(db_column='ASAM2', blank=True, null=True)

    asam2_5 = models.IntegerField(db_column='ASAM2_5', blank=True, null=True)

    asam3 = models.IntegerField(db_column='ASAM3', blank=True, null=True)

    asam4 = models.IntegerField(db_column='ASAM4', blank=True, null=True)

    modrisk = models.IntegerField(db_column='ModRisk', blank=True, null=True)

    highrisk = models.IntegerField(db_column='HighRisk', blank=True, null=True)

    judstatushearings = models.IntegerField(
        db_column='JudStatusHearings', blank=True, null=True)

    phase1 = models.IntegerField(db_column='Phase1', blank=True, null=True)

    phase2 = models.IntegerField(db_column='Phase2', blank=True, null=True)

    phase3 = models.IntegerField(db_column='Phase3', blank=True, null=True)

    phase4 = models.IntegerField(db_column='Phase4', blank=True, null=True)

    phase5 = models.IntegerField(db_column='Phase5', blank=True, null=True)

    su_o1name = models.IntegerField(
        db_column='SU_O1Name', blank=True, null=True)

    su_o2name = models.IntegerField(
        db_column='SU_O2Name', blank=True, null=True)

    sa_o1name = models.IntegerField(
        db_column='SA_O1Name', blank=True, null=True)

    sa_o2name = models.IntegerField(
        db_column='SA_O2Name', blank=True, null=True)

    rejected1 = models.IntegerField(
        db_column='Rejected1', blank=True, null=True)

    graduated = models.IntegerField(
        db_column='Graduated', blank=True, null=True)

    datastart = models.DateField(db_column='DataStart', blank=True, null=True)

    dataend = models.DateField(db_column='DataEnd', blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    id = models.AutoField(db_column='ID', primary_key=True)

    acceptedprobrev = models.IntegerField(
        db_column='AcceptedProbRev', blank=True, null=True)

    rejected1descrip = models.CharField(
        db_column='Rejected1Descrip', max_length=25, blank=True, null=True)

    rejected2descrip = models.CharField(
        db_column='Rejected2Descrip', max_length=25, blank=True, null=True)

    rejected3descrip = models.CharField(
        db_column='Rejected3Descrip', max_length=25, blank=True, null=True)

    rejected4descrip = models.CharField(
        db_column='Rejected4Descrip', max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'GenInfo'


class Housing(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    housingname = models.CharField(
        db_column='HousingName', max_length=75, blank=True, null=True)

    housingrentamount = models.DecimalField(
        db_column='HousingRentAmount', max_digits=19, decimal_places=4, blank=True, null=True)

    housingaddress1 = models.CharField(
        db_column='HousingAddress1', max_length=50, blank=True, null=True)

    housingaddress2 = models.CharField(
        db_column='HousingAddress2', max_length=50, blank=True, null=True)

    housingcitystatezip = models.CharField(
        db_column='HousingCityStateZip', max_length=50)

    class Meta:
        managed = True
        db_table = 'Housing'


class Incomeranges(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    incomerange = models.CharField(db_column='IncomeRange', max_length=50)

    class Meta:
        managed = True
        db_table = 'IncomeRanges'


class Judges(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    division = models.SmallIntegerField(db_column='Division')

    judgename = models.CharField(db_column='JudgeName', max_length=55)

    judgeemail = models.CharField(
        db_column='JudgeEmail', max_length=75, blank=True, null=True)

    assistantname = models.CharField(
        db_column='AssistantName', max_length=50, blank=True, null=True)

    assistantemail = models.CharField(
        db_column='AssistantEmail', max_length=75, blank=True, null=True)

    phone = models.CharField(
        db_column='Phone', max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Judges'


class Lsitypes(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    lsitype = models.CharField(
        db_column='LSIType', max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'LSITypes'


class Mhphysicians(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    mhphysicianname = models.CharField(
        db_column='MHPhysicianName', max_length=50)

    mhfacilityname = models.CharField(
        db_column='MHFacilityName', max_length=50, blank=True, null=True)

    mhaddress = models.CharField(
        db_column='MHAddress', max_length=50, blank=True, null=True)

    mhcity = models.CharField(db_column='MHCity', max_length=25)

    mhstate = models.CharField(db_column='MHState', max_length=2)

    mhzip = models.CharField(
        db_column='MHZip', max_length=10, blank=True, null=True)

    mhphone = models.CharField(
        db_column='MHPhone', max_length=15, blank=True, null=True)

    mhpdate = models.DateTimeField(db_column='MHPDate', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'MHPhysicians'


class Mentalhealth(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    evaldate = models.DateTimeField(
        db_column='EvalDate', blank=True, null=True)

    comments = models.TextField(db_column='Comments', blank=True, null=True)

    medications = models.CharField(
        db_column='Medications', max_length=50, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = True
        db_table = 'MentalHealth'


class Objectives(models.Model):

    objid = models.AutoField(db_column='ObjID', primary_key=True)

    clientobjnum = models.IntegerField(
        db_column='ClientObjNum', blank=True, null=True)

    probgoalid = models.ForeignKey(
        'Probgoals', models.DO_NOTHING, db_column='ProbGoalID', blank=True, null=True)

    clientid = models.CharField(
        db_column='ClientID', max_length=15, blank=True, null=True)

    obj = models.CharField(
        db_column='Obj', max_length=150, blank=True, null=True)

    objtarget = models.DateTimeField(
        db_column='ObjTarget', blank=True, null=True)

    intervention1 = models.CharField(
        db_column='Intervention1', max_length=150, blank=True, null=True)

    intervention2 = models.CharField(
        db_column='Intervention2', max_length=150, blank=True, null=True)

    closed = models.BooleanField(db_column='Closed')
    met = models.BooleanField(db_column='Met')

    metdate = models.DateTimeField(db_column='MetDate', blank=True, null=True)

    rating = models.CharField(
        db_column='Rating', max_length=1, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    objtype = models.CharField(
        db_column='ObjType', max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Objectives'


class Outreach(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    outreachdate = models.CharField(db_column='OutreachDate', max_length=50)

    outreachhours = models.SmallIntegerField(db_column='OutreachHours')

    outreachdescription = models.CharField(
        db_column='OutreachDescription', max_length=50)

    outreachverifiedby = models.CharField(
        db_column='OutreachVerifiedBy', max_length=50, blank=True, null=True)

    type = models.CharField(
        db_column='Type', max_length=15, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Outreach'


class Phases(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    phase = models.CharField(db_column='Phase', max_length=10)

    track = models.CharField(
        db_column='Track', max_length=2, blank=True, null=True)

    site = models.CharField(
        db_column='Site', max_length=50, blank=True, null=True)

    screensperweek = models.IntegerField(
        db_column='ScreensPerWeek', blank=True, null=True)

    stepsessionsperweek = models.IntegerField(
        db_column='StepSessionsPerWeek', blank=True, null=True)

    meetingsperweek = models.IntegerField(
        db_column='MeetingsPerWeek', blank=True, null=True)

    courtperiod = models.CharField(
        db_column='CourtPeriod', max_length=15, blank=True, null=True)

    txsessionsperperiod = models.IntegerField(
        db_column='TxSessionsPerPeriod', blank=True, null=True)

    txsessionhrs = models.FloatField(
        db_column='TxSessionHrs', blank=True, null=True)

    step = models.IntegerField(db_column='Step', blank=True, null=True)

    other = models.IntegerField(db_column='Other', blank=True, null=True)

    minphasedays = models.IntegerField(
        db_column='MinPhaseDays', blank=True, null=True)

    casereviewfreq = models.CharField(
        db_column='CaseReviewFreq', max_length=15, blank=True, null=True)

    weeklyfees = models.DecimalField(
        db_column='WeeklyFees', max_digits=19, decimal_places=4, blank=True, null=True)

    cumfees = models.DecimalField(
        db_column='CumFees', max_digits=19, decimal_places=4, blank=True, null=True)

    employmenthrs = models.IntegerField(
        db_column='EmploymentHrs', blank=True, null=True)

    courtdateday = models.IntegerField(
        db_column='CourtDateDay', blank=True, null=True)

    grpnotes = models.IntegerField(db_column='GrpNotes', blank=True, null=True)

    grpnotefreq = models.CharField(
        db_column='GrpNoteFreq', max_length=15, blank=True, null=True)

    indsession = models.IntegerField(
        db_column='IndSession', blank=True, null=True)

    feebalancealert = models.DecimalField(
        db_column='FeeBalanceAlert', max_digits=19, decimal_places=4, blank=True, null=True)

    courtfreqency = models.CharField(
        db_column='CourtFreqency', max_length=15, blank=True, null=True)

    minimumdays = models.IntegerField(
        db_column='MinimumDays', blank=True, null=True)

    casereview = models.CharField(
        db_column='CaseReview', max_length=15, blank=True, null=True)

    fees = models.DecimalField(
        db_column='Fees', max_digits=19, decimal_places=4, blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = True
        db_table = 'Phases'


class Physicians(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    physicianname = models.CharField(
        db_column='PhysicianName', max_length=50, blank=True, null=True)

    facilityname = models.CharField(
        db_column='FacilityName', max_length=50, blank=True, null=True)

    physicianaddress = models.CharField(
        db_column='PhysicianAddress', max_length=50, blank=True, null=True)

    physiciancity = models.CharField(
        db_column='PhysicianCity', max_length=50, blank=True, null=True)

    physicianstate = models.CharField(
        db_column='PhysicianState', max_length=2, blank=True, null=True)

    physicianzip = models.CharField(
        db_column='PhysicianZip', max_length=10, blank=True, null=True)

    physicianphone = models.CharField(
        db_column='PhysicianPhone', max_length=50, blank=True, null=True)

    physiciandates = models.CharField(
        db_column='PhysicianDates', max_length=50, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Physicians'


class Positivetypes(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    description = models.CharField(db_column='Description', max_length=50)

    column2 = models.CharField(
        db_column='Column2', max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PositiveTypes'


class Priortx(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    type = models.CharField(db_column='Type', max_length=30)

    description = models.CharField(db_column='Description', max_length=30)

    provider = models.CharField(
        db_column='Provider', max_length=50, blank=True, null=True)

    provideraddress = models.CharField(
        db_column='ProviderAddress', max_length=60, blank=True, null=True)

    providercity = models.CharField(
        db_column='ProviderCity', max_length=50, blank=True, null=True)

    providerstate = models.CharField(
        db_column='ProviderState', max_length=2, blank=True, null=True)

    providerzip = models.CharField(
        db_column='ProviderZip', max_length=10, blank=True, null=True)

    providerphone = models.CharField(
        db_column='ProviderPhone', max_length=15, blank=True, null=True)

    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)

    outcome = models.CharField(
        db_column='Outcome', max_length=100, blank=True, null=True)

    yearssober = models.IntegerField(
        db_column='YearsSober', blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PriorTx'


class Probgoals(models.Model):

    probgoalid = models.AutoField(db_column='ProbGoalID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    disciplineid = models.IntegerField(db_column='DisciplineID')

    probgoalnum = models.IntegerField(db_column='ProbGoalNum')

    prob = models.CharField(db_column='Prob', max_length=100)

    goal = models.CharField(db_column='Goal', max_length=150)

    probgoaltarget = models.DateTimeField(db_column='ProbGoalTarget')

    probgoaltype = models.CharField(db_column='ProbGoalType', max_length=15)

    probgoalstatus = models.CharField(
        db_column='ProbGoalStatus', max_length=20)

    resolveddate = models.DateTimeField(
        db_column='ResolvedDate', blank=True, null=True)

    deferreddate = models.DateTimeField(
        db_column='DeferredDate', blank=True, null=True)

    closeddate = models.DateTimeField(
        db_column='ClosedDate', blank=True, null=True)

    lsir = models.CharField(
        db_column='LSIR', max_length=50, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ProbGoals'


class Proposals(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    proposaltype = models.CharField(db_column='ProposalType', max_length=15)

    proposaldate = models.DateField(db_column='ProposalDate')

    passstart = models.CharField(
        db_column='PassStart', max_length=10, blank=True, null=True)

    passend = models.CharField(
        db_column='PassEnd', max_length=10, blank=True, null=True)

    proposaldescription = models.CharField(
        db_column='ProposalDescription', max_length=255, blank=True, null=True)

    proposalstatus = models.CharField(
        db_column='ProposalStatus', max_length=15, blank=True, null=True)

    proposalcomment = models.CharField(
        db_column='ProposalComment', max_length=255, blank=True, null=True)

    laststatusdate = models.DateField(
        db_column='LastStatusDate', blank=True, null=True)

    approver = models.CharField(
        db_column='Approver', max_length=25, blank=True, null=True)

    approvedate = models.DateField(
        db_column='ApproveDate', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    passdate = models.DateField(db_column='Passdate', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Proposals'


class Race(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    racetitle = models.CharField(
        db_column='RaceTitle', max_length=35, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Race'


class Ratinghistory(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    ratingdate = models.DateTimeField(
        db_column='RatingDate', blank=True, null=True)

    probgoalid = models.IntegerField(
        db_column='ProbGoalID', blank=True, null=True)

    objid = models.IntegerField(db_column='ObjID', blank=True, null=True)

    sort = models.IntegerField(db_column='Sort', blank=True, null=True)

    description = models.CharField(
        db_column='Description', max_length=150, blank=True, null=True)

    crating = models.CharField(
        db_column='CRating', max_length=1, blank=True, null=True)

    prating = models.CharField(
        db_column='PRating', max_length=1, blank=True, null=True)

    rater = models.CharField(
        db_column='Rater', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    problemid = models.IntegerField(
        db_column='ProblemID', blank=True, null=True)

    objectiveid = models.IntegerField(
        db_column='ObjectiveID', blank=True, null=True)

    currentphase = models.CharField(
        db_column='CurrentPhase', max_length=2, blank=True, null=True)

    phasedays = models.IntegerField(
        db_column='PhaseDays', blank=True, null=True)

    nextratingdate = models.DateTimeField(
        db_column='NextRatingDate', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'RatingHistory'


class Rejectreasons(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    rejectreason = models.CharField(
        db_column='RejectReason', max_length=50, blank=True, null=True)

    sort = models.IntegerField(db_column='Sort', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'RejectReasons'


class Rewards(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    courtid = models.ForeignKey(
        Court, models.DO_NOTHING, db_column='CourtID', blank=True, null=True)

    rewarddate = models.DateTimeField(
        db_column='RewardDate', blank=True, null=True)

    rewarddescription = models.CharField(
        db_column='RewardDescription', max_length=50, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    clientid = models.CharField(
        db_column='ClientID', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Rewards'


class Sanctionlevels(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    sanctionlevel = models.CharField(db_column='SanctionLevel', max_length=50)

    class Meta:
        managed = True
        db_table = 'SanctionLevels'
        app_label = 'cases'


class Sanctions(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    sanctionlevel = models.CharField(db_column='SanctionLevel', max_length=50)

    sanctiondate = models.DateTimeField(
        db_column='SanctionDate', blank=True, null=True)

    description = models.CharField(
        db_column='Description', max_length=255, blank=True, null=True)

    daysinjail = models.SmallIntegerField(
        db_column='DaysInJail', blank=True, null=True)

    datejailstart = models.DateTimeField(
        db_column='DateJailStart', blank=True, null=True)

    datejailend = models.DateTimeField(
        db_column='DateJailEnd', blank=True, null=True)

    csprovider = models.CharField(
        db_column='CSProvider', max_length=50, blank=True, null=True)

    csdate = models.CharField(
        db_column='CSDate', max_length=50, blank=True, null=True)

    cshoursrequired = models.SmallIntegerField(
        db_column='CSHoursRequired', blank=True, null=True)

    cshourscompleted = models.SmallIntegerField(
        db_column='CSHoursCompleted', blank=True, null=True)

    csverifiedby = models.CharField(
        db_column='CSVerifiedBy', max_length=55, blank=True, null=True)

    complete = models.BooleanField(db_column='Complete', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    level4complete = models.BooleanField(db_column='Level4Complete')
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = True
        db_table = 'Sanctions'


class Screensimport(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    accession = models.IntegerField(
        db_column='Accession', blank=True, null=True)

    clientid = models.CharField(
        db_column='ClientID', max_length=50, blank=True, null=True)

    collectdate = models.DateTimeField(
        db_column='CollectDate', blank=True, null=True)

    testdate = models.DateTimeField(
        db_column='TestDate', blank=True, null=True)

    result = models.CharField(
        db_column='Result', max_length=255, blank=True, null=True)

    drugsfound = models.CharField(
        db_column='Drugsfound', max_length=255, blank=True, null=True)

    notes = models.CharField(
        db_column='Notes', max_length=255, blank=True, null=True)

    agency = models.CharField(
        db_column='Agency', max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ScreensImport'


class Screenslab(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    agency = models.CharField(
        db_column='Agency', max_length=50, blank=True, null=True)

    accession = models.IntegerField(db_column='Accession')

    collectdate = models.DateTimeField(
        db_column='CollectDate', blank=True, null=True)

    testdate = models.DateTimeField(
        db_column='TestDate', blank=True, null=True)

    result = models.CharField(
        db_column='Result', max_length=255, blank=True, null=True)

    resultconfirmed = models.BooleanField(db_column='ResultConfirmed')

    positiveapproved = models.BooleanField(db_column='PositiveApproved')

    drugsfound = models.CharField(
        db_column='DrugsFound', max_length=255, blank=True, null=True)

    notes = models.CharField(
        db_column='Notes', max_length=255, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    positivetype = models.CharField(
        db_column='PositiveType', max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ScreensLab'


class Screensother(models.Model):

    clientid = models.CharField(db_column='ClientID', max_length=15)

    collectdate = models.DateTimeField(db_column='CollectDate')

    result = models.CharField(
        db_column='Result', max_length=25, blank=True, null=True)

    resultconfirmed = models.BooleanField(
        db_column='ResultConfirmed', blank=True, null=True)

    positiveapproved = models.BooleanField(db_column='PositiveApproved')

    noshow = models.BooleanField(db_column='NoShow')

    drugsfound = models.CharField(
        db_column='DrugsFound', max_length=100, blank=True, null=True)

    notes = models.CharField(
        db_column='Notes', max_length=255, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    id = models.AutoField(db_column='ID', primary_key=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    refusal = models.BooleanField(db_column='Refusal', blank=True, null=True)

    diluted = models.BooleanField(db_column='Diluted', blank=True, null=True)

    admitted = models.BooleanField(db_column='Admitted', blank=True, null=True)

    positivetype = models.CharField(
        db_column='PositiveType', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ScreensOther'


class Status(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    statusmsg = models.CharField(
        db_column='StatusMsg', max_length=25, blank=True, null=True)

    msgtype = models.CharField(
        db_column='MsgType', max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Status'


class Stepattendance(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    weekstart = models.DateField(db_column='WeekStart', blank=True, null=True)

    attended = models.IntegerField(db_column='Attended', blank=True, null=True)

    comment = models.CharField(
        db_column='Comment', max_length=255, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    modified = models.DateTimeField(
        db_column='Modified', blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    required = models.IntegerField(db_column='Required', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'StepAttendance'


class Substanceuse(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    aod = models.CharField(
        db_column='AOD', max_length=20, blank=True, null=True)

    route = models.CharField(
        db_column='Route', max_length=15, blank=True, null=True)

    frequency = models.CharField(
        db_column='Frequency', max_length=15, blank=True, null=True)

    agebegan = models.IntegerField(db_column='AgeBegan', blank=True, null=True)

    lastuse = models.CharField(
        db_column='LastUse', max_length=15, blank=True, null=True)

    comments = models.CharField(
        db_column='Comments', max_length=250, blank=True, null=True)

    usebyfamily = models.BooleanField(db_column='UseByFamily')

    usebypartner = models.BooleanField(db_column='UseByPartner')

    currentlyused = models.BooleanField(db_column='CurrentlyUsed')

    costperweek = models.DecimalField(
        db_column='CostPerWeek', max_digits=19, decimal_places=4, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = True
        db_table = 'SubstanceUse'


class Tempnote(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    tempnote = models.TextField(db_column='TempNote', blank=True, null=True)

    notedate = models.DateTimeField(
        db_column='NoteDate', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    createdate = models.DateTimeField(
        db_column='CreateDate', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TempNote'


class Temprating(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    ratingdate = models.DateTimeField(
        db_column='RatingDate', blank=True, null=True)

    probgoalid = models.IntegerField(db_column='ProbGoalID')

    objid = models.IntegerField(db_column='ObjID', blank=True, null=True)

    sort = models.IntegerField(db_column='Sort', blank=True, null=True)

    description = models.CharField(
        db_column='Description', max_length=150, blank=True, null=True)

    crating = models.CharField(
        db_column='CRating', max_length=1, blank=True, null=True)

    prating = models.CharField(
        db_column='PRating', max_length=1, blank=True, null=True)

    rater = models.CharField(
        db_column='Rater', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TempRating'


class Temptxattendance(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    name = models.CharField(
        db_column='Name', max_length=50, blank=True, null=True)

    sessiondate = models.DateTimeField(
        db_column='SessionDate', blank=True, null=True)

    aaorna = models.BooleanField(db_column='AAorNA', blank=True, null=True)

    attendance = models.BooleanField(
        db_column='Attendance', blank=True, null=True)

    attendancecomments = models.CharField(
        db_column='AttendanceComments', max_length=255, blank=True, null=True)

    reason = models.CharField(
        db_column='Reason', max_length=10, blank=True, null=True)

    txid = models.IntegerField(db_column='TxID', blank=True, null=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    timein = models.CharField(
        db_column='TimeIn', max_length=11, blank=True, null=True)

    timeout = models.CharField(
        db_column='Timeout', max_length=11, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = True
        db_table = 'TempTxAttendance'


class Temptxnotes(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    lfname = models.CharField(
        db_column='LFName', max_length=50, blank=True, null=True)

    note = models.TextField(db_column='Note', blank=True, null=True)

    notetype = models.CharField(
        db_column='NoteType', max_length=15, blank=True, null=True)

    notedate = models.DateTimeField(
        db_column='NoteDate', blank=True, null=True)

    probgoalnum = models.CharField(
        db_column='ProbGoalNum', max_length=50, blank=True, null=True)

    timein = models.CharField(
        db_column='TimeIn', max_length=11, blank=True, null=True)

    timeout = models.CharField(
        db_column='TimeOut', max_length=11, blank=True, null=True)

    reason = models.CharField(
        db_column='Reason', max_length=11, blank=True, null=True)

    nrd = models.DateTimeField(db_column='NRD', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = True
        db_table = 'TempTxNotes'


class Txattendance(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)

    sessiondate = models.DateTimeField(db_column='SessionDate')

    attendedyn = models.BooleanField(
        db_column='AttendedYN', blank=True, null=True)

    nonattendreason = models.CharField(
        db_column='NonAttendReason', max_length=10, blank=True, null=True)

    timein = models.CharField(
        db_column='TimeIn', max_length=11, blank=True, null=True)

    timeout = models.CharField(
        db_column='TimeOut', max_length=11, blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = True
        db_table = 'TxAttendance'


class Txnotes(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    clientid = models.CharField(db_column='ClientID', max_length=15)
    note = models.TextField(db_column='Note')

    notetype = models.CharField(db_column='NoteType', max_length=15)

    notedate = models.DateTimeField(db_column='NoteDate')

    probgoalnum = models.CharField(
        db_column='ProbGoalNum', max_length=50, blank=True, null=True)

    timein = models.CharField(
        db_column='TimeIn', max_length=11, blank=True, null=True)

    timeout = models.CharField(
        db_column='TimeOut', max_length=11, blank=True, null=True)

    reason = models.CharField(
        db_column='Reason', max_length=10, blank=True, null=True)

    nrd = models.DateTimeField(db_column='NRD', blank=True, null=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    notetoclient = models.TextField(
        db_column='NoteToClient', blank=True, null=True)

    phase = models.CharField(
        db_column='Phase', max_length=1, blank=True, null=True)

    discipline = models.CharField(
        db_column='Discipline', max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TxNotes'


class Userinfo(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    userid = models.CharField(db_column='UserID', max_length=25)

    username = models.CharField(
        db_column='UserName', max_length=55, blank=True, null=True)

    roleid = models.IntegerField(db_column='RoleID')

    useremail = models.CharField(
        db_column='UserEmail', max_length=75, blank=True, null=True)

    userphone = models.CharField(
        db_column='UserPhone', max_length=15, blank=True, null=True)

    active = models.BooleanField(db_column='Active', blank=True, null=True)

    defaulttrack = models.CharField(
        db_column='DefaultTrack', max_length=1, blank=True, null=True)

    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = True
        db_table = 'UserInfo'


class Userlogininfo(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    ip = models.CharField(db_column='IP', max_length=20, blank=True, null=True)

    startsession = models.DateTimeField(
        db_column='StartSession', blank=True, null=True)

    finishsession = models.DateTimeField(
        db_column='FinishSession', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'UserLoginInfo'
