# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django_fsm import FSMField, transition
from django.urls import reverse


class Appinfo(models.Model):
    # Field name made lowercase.
    orgname = models.CharField(
        db_column='OrgName', primary_key=True, max_length=50)
    # Field name made lowercase.
    apppath = models.CharField(
        db_column='AppPath', max_length=75, blank=True, null=True)
    # Field name made lowercase.
    photopath = models.CharField(
        db_column='PhotoPath', max_length=75, blank=True, null=True)
    # Field name made lowercase.
    track = models.CharField(
        db_column='Track', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    site = models.CharField(
        db_column='Site', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    datastart = models.DateTimeField(
        db_column='DataStart', blank=True, null=True)
    # Field name made lowercase.
    type = models.CharField(
        db_column='Type', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    judge = models.CharField(
        db_column='Judge', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    coordinator = models.CharField(
        db_column='Coordinator', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    docpath = models.CharField(
        db_column='DocPath', max_length=125, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AppInfo'


class Approles(models.Model):
    # Field name made lowercase.
    roleid = models.AutoField(db_column='RoleID', primary_key=True)
    # Field name made lowercase.
    roletitle = models.CharField(
        db_column='RoleTitle', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    disciplineid = models.IntegerField(
        db_column='DisciplineID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AppRoles'


class Assessments(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    assessdate = models.DateField(
        db_column='AssessDate', blank=True, null=True)
    # Field name made lowercase.
    assessscore = models.IntegerField(
        db_column='AssessScore', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    assesstool = models.CharField(
        db_column='AssessTool', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Assessments'


class Attorneys(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    attorneyname = models.CharField(db_column='AttorneyName', max_length=55)
    # Field name made lowercase.
    attorneytype = models.CharField(
        db_column='AttorneyType', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='Email', max_length=75, blank=True, null=True)
    # Field name made lowercase.
    phone = models.CharField(
        db_column='Phone', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Attorneys'


class Cs(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    csdate = models.DateTimeField(db_column='CSDate')
    # Field name made lowercase.
    csassignment = models.CharField(
        db_column='CSAssignment', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cshours = models.SmallIntegerField(db_column='CSHours')
    # Field name made lowercase.
    csverifiedby = models.CharField(
        db_column='CSVerifiedBy', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CS'


class Casenums(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    casenum = models.CharField(db_column='CaseNum', max_length=11)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    charges = models.CharField(
        db_column='Charges', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    arrestdate = models.DateTimeField(
        db_column='ArrestDate', blank=True, null=True)
    # Field name made lowercase.
    dispositiondate = models.DateTimeField(
        db_column='DispositionDate', blank=True, null=True)
    # Field name made lowercase.
    disposition = models.CharField(
        db_column='Disposition', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    division = models.IntegerField(db_column='Division', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CaseNums'


class Children(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    childgender = models.CharField(db_column='ChildGender', max_length=50)
    # Field name made lowercase.
    name = models.CharField(
        db_column='Name', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    childdob = models.DateTimeField(
        db_column='ChildDOB', blank=True, null=True)
    # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=8,
                           blank=True, null=True)
    # Field name made lowercase.
    contact = models.CharField(
        db_column='Contact', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    custody = models.CharField(
        db_column='Custody', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cpscase = models.CharField(
        db_column='CPSCase', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    home = models.CharField(
        db_column='Home', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    otherhome = models.CharField(
        db_column='OtherHome', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Children'


class Chroniccond(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    condition = models.CharField(
        db_column='Condition', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    diagnosis = models.TextField(db_column='Diagnosis', blank=True, null=True)
    # Field name made lowercase.
    physician = models.CharField(
        db_column='Physician', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='userID', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = False
        db_table = 'ChronicCond'


class Clientaddress(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    activedate = models.DateTimeField(db_column='Activedate')
    # Field name made lowercase.
    residencetype = models.CharField(db_column='ResidenceType', max_length=25)
    # Field name made lowercase.
    address1 = models.CharField(
        db_column='Address1', max_length=75, blank=True, null=True)
    # Field name made lowercase.
    address2 = models.CharField(
        db_column='Address2', max_length=75, blank=True, null=True)
    # Field name made lowercase.
    city = models.CharField(
        db_column='City', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    state = models.CharField(
        db_column='State', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    zip = models.CharField(
        db_column='Zip', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    homephone = models.CharField(
        db_column='HomePhone', max_length=14, blank=True, null=True)
    # Field name made lowercase.
    contact = models.CharField(
        db_column='Contact', max_length=20, blank=True, null=True)
    payment = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ClientAddress'


class Clientcontacts(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    clientrelationship = models.CharField(
        db_column='ClientRelationship', max_length=20)
    # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=20)
    # Field name made lowercase.
    contactphone1 = models.CharField(
        db_column='ContactPhone1', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    contactphone2 = models.CharField(
        db_column='ContactPhone2', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    contactaddress = models.CharField(
        db_column='ContactAddress', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    contactcitystatezip = models.CharField(
        db_column='ContactCityStateZip', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ClientContacts'


class Clientdocs(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=25)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    docname = models.CharField(
        db_column='DocName', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    docdate = models.DateField(db_column='DocDate', blank=True, null=True)
    # Field name made lowercase.
    doclink = models.CharField(
        db_column='DocLink', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    docnote = models.CharField(
        db_column='DocNote', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ClientDocs'


class Clientlog(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    changedate = models.DateTimeField(db_column='ChangeDate')
    # Field name made lowercase.
    changefield = models.CharField(db_column='ChangeField', max_length=255)
    # Field name made lowercase.
    changeinfo = models.CharField(db_column='ChangeInfo', max_length=255)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ClientLog'


class Clientphase(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    phase = models.CharField(db_column='Phase', max_length=1)
    # Field name made lowercase.
    phasestart = models.DateTimeField(db_column='PhaseStart')
    # Field name made lowercase.
    phaseend = models.DateTimeField(
        db_column='PhaseEnd', blank=True, null=True)
    completed = models.BooleanField(blank=True, null=True)
    # Field name made lowercase.
    totaldays = models.IntegerField(
        db_column='TotalDays', blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = False
        db_table = 'ClientPhase'


class Clients(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(
        db_column='ClientID', unique=True, max_length=15)
    # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)
    # Field name made lowercase.
    dischargedate = models.DateField(
        db_column='DischargeDate', blank=True, null=True)
    # Field name made lowercase.
    cellphone = models.CharField(
        db_column='CellPhone', max_length=50, blank=True, null=True)
    # Change to Email Validator
    # Field name made lowercase.
    email = models.CharField(
        db_column='Email', max_length=75, blank=True, null=True)
    # Field name made lowercase.
    message = models.CharField(
        db_column='Message', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    messagesource = models.CharField(
        db_column='MessageSource', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    yearlyincome = models.CharField(
        db_column='YearlyIncome', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    incomesource = models.CharField(
        db_column='IncomeSource', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    educationyrs = models.IntegerField(
        db_column='EducationYrs', blank=True, null=True)
    # Field name made lowercase.
    educationlevel = models.CharField(
        db_column='EducationLevel', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    highschoolgrad = models.CharField(
        db_column='HighSchoolGrad', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    ged = models.CharField(db_column='GED', max_length=3,
                           blank=True, null=True)
    # Field name made lowercase.
    militaryservice = models.BooleanField(db_column='MilitaryService')
    # Field name made lowercase.
    vaeligible = models.BooleanField(db_column='VAEligible')
    # Field name made lowercase.
    maritalstatus = models.CharField(
        db_column='MaritalStatus', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    pregnant = models.CharField(
        db_column='Pregnant', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    children = models.CharField(
        db_column='Children', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    childnarrative = models.TextField(
        db_column='ChildNarrative', blank=True, null=True)
    # Field name made lowercase.
    diagnosis = models.TextField(db_column='Diagnosis', blank=True, null=True)
    # Field name made lowercase.
    suicide = models.BooleanField(db_column='Suicide')
    # Field name made lowercase.
    violence = models.BooleanField(db_column='Violence')
    # Field name made lowercase.
    health = models.TextField(db_column='Health', blank=True, null=True)
    # Field name made lowercase.
    ghmedications = models.TextField(
        db_column='GhMedications', blank=True, null=True)
    # Field name made lowercase.
    prenatal = models.TextField(db_column='Prenatal', blank=True, null=True)
    # Field name made lowercase.
    tbstatus = models.CharField(
        db_column='TBStatus', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    physicalabuse = models.BooleanField(db_column='PhysicalAbuse')
    # Field name made lowercase.
    sexualabuse = models.BooleanField(db_column='SexualAbuse')
    # Field name made lowercase.
    insurance = models.CharField(
        db_column='Insurance', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    primarydrug = models.CharField(
        db_column='PrimaryDrug', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    substanceuse = models.CharField(
        db_column='SubstanceUse', max_length=6, blank=True, null=True)
    # Field name made lowercase.
    sobriety = models.CharField(
        db_column='Sobriety', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    needleuse = models.BooleanField(db_column='NeedleUse')
    # Field name made lowercase.
    addictionseverityindex = models.CharField(
        db_column='AddictionSeverityIndex', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    familyoforiginyn = models.BooleanField(db_column='FamilyofOriginYN')
    # Field name made lowercase.
    familyoforiginuse = models.CharField(
        db_column='FamilyofOriginUse', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    spouseuseyn = models.BooleanField(db_column='SpouseUseYN')
    # Field name made lowercase.
    spouseuse = models.CharField(
        db_column='SpouseUse', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    testtype = models.CharField(
        db_column='TestType', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    testresults = models.CharField(
        db_column='TestResults', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    employedatgraduation = models.BooleanField(
        db_column='EmployedAtGraduation', blank=True, null=True)
    # Field name made lowercase.
    outcomecomments = models.TextField(
        db_column='OutcomeComments', blank=True, null=True)
    # Field name made lowercase.
    cmuserid = models.CharField(
        db_column='CMUserID', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    couserid = models.CharField(
        db_column='COUserID', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    phase = models.CharField(
        db_column='Phase', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    stopbilling = models.BooleanField(
        db_column='StopBilling', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')
    # Field name made lowercase.
    lastpositive = models.DateField(
        db_column='LastPositive', blank=True, null=True)
    # Field name made lowercase.
    lep = models.IntegerField(db_column='LEP', blank=True, null=True)
    # Field name made lowercase.
    employedatstart = models.CharField(
        db_column='EmployedAtStart', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    employedatgrad = models.CharField(
        db_column='EmployedAtGrad', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    asam_loc = models.DecimalField(
        db_column='ASAM_LOC', max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Clients'
        verbose_name_plural = 'clients'


class Court(models.Model):
    # Field name made lowercase.
    courtid = models.AutoField(db_column='CourtID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    courtdate = models.DateTimeField(db_column='CourtDate')
    # Field name made lowercase.
    event = models.CharField(
        db_column='Event', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    courtdatetype = models.CharField(
        db_column='CourtDateType', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    phase = models.CharField(
        db_column='Phase', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    attendance = models.CharField(
        db_column='Attendance', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=15, blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = False
        db_table = 'Court'


class Crimhistory(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    charge = models.CharField(
        db_column='Charge', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    chargetype = models.CharField(
        db_column='ChargeType', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    penalcode = models.CharField(
        db_column='PenalCode', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    status = models.CharField(
        db_column='Status', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    chargedate = models.DateTimeField(
        db_column='ChargeDate', blank=True, null=True)
    # Field name made lowercase.
    chargenote = models.CharField(
        db_column='ChargeNote', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CrimHistory'


class Dblog(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    logdate = models.DateField(db_column='LogDate', blank=True, null=True)
    # Field name made lowercase.
    track = models.CharField(
        db_column='Track', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    cntpending = models.IntegerField(
        db_column='CntPending', blank=True, null=True)
    # Field name made lowercase.
    cntactive = models.IntegerField(
        db_column='CntActive', blank=True, null=True)
    # Field name made lowercase.
    cntawol = models.IntegerField(db_column='CntAWOL', blank=True, null=True)
    # Field name made lowercase.
    cntpendingterm = models.IntegerField(
        db_column='CntPendingTerm', blank=True, null=True)
    # Field name made lowercase.
    cntincustody = models.IntegerField(
        db_column='CntInCustody', blank=True, null=True)
    # Field name made lowercase.
    cntmedicalleave = models.IntegerField(
        db_column='CntMedicalLeave', blank=True, null=True)
    # Field name made lowercase.
    cntpositivescreens = models.IntegerField(
        db_column='CntPositiveScreens', blank=True, null=True)
    # Field name made lowercase.
    cntoverinphase = models.IntegerField(
        db_column='CntOverInPhase', blank=True, null=True)
    # Field name made lowercase.
    cntphalert = models.IntegerField(
        db_column='CntPhAlert', blank=True, null=True)
    # Field name made lowercase.
    cntfeesalert = models.IntegerField(
        db_column='CntFeesAlert', blank=True, null=True)
    # Field name made lowercase.
    cntstepup = models.IntegerField(
        db_column='CntStepUp', blank=True, null=True)
    # Field name made lowercase.
    cntproposals = models.IntegerField(
        db_column='CntProposals', blank=True, null=True)
    # Field name made lowercase.
    cnt12step = models.IntegerField(
        db_column='Cnt12Step', blank=True, null=True)
    # Field name made lowercase.
    cntnrd = models.IntegerField(db_column='CntNRD', blank=True, null=True)
    # Field name made lowercase.
    cntsessions = models.IntegerField(
        db_column='CntSessions', blank=True, null=True)
    # Field name made lowercase.
    cntobjectivesdue = models.IntegerField(
        db_column='CntObjectivesDue', blank=True, null=True)
    # Field name made lowercase.
    cntratingsdue = models.IntegerField(
        db_column='CntRatingsDue', blank=True, null=True)
    # Field name made lowercase.
    cntnotesdue = models.IntegerField(
        db_column='CntNotesDue', blank=True, null=True)
    # Field name made lowercase.
    cntcourtdates = models.IntegerField(
        db_column='CntCourtDates', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DBLog'


class Dashboard(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    cntdate = models.DateTimeField(db_column='CntDate', blank=True, null=True)
    # Field name made lowercase.
    track = models.CharField(
        db_column='Track', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    site = models.CharField(db_column='Site', max_length=40)
    # Field name made lowercase.
    cntpending = models.IntegerField(
        db_column='CntPending', blank=True, null=True)
    # Field name made lowercase.
    cntactive = models.IntegerField(
        db_column='CntActive', blank=True, null=True)
    # Field name made lowercase.
    cntawol = models.IntegerField(db_column='CntAWOL', blank=True, null=True)
    # Field name made lowercase.
    cntpendingterm = models.IntegerField(
        db_column='CntPendingTerm', blank=True, null=True)
    # Field name made lowercase.
    cntincustody = models.IntegerField(
        db_column='CntInCustody', blank=True, null=True)
    # Field name made lowercase.
    cntmedicalleave = models.IntegerField(
        db_column='CntMedicalLeave', blank=True, null=True)
    # Field name made lowercase.
    cntpositivescreens = models.IntegerField(
        db_column='CntPositiveScreens', blank=True, null=True)
    # Field name made lowercase.
    cntoverinphase = models.IntegerField(
        db_column='CntOverInPhase', blank=True, null=True)
    # Field name made lowercase.
    cntphalert = models.IntegerField(
        db_column='CntPhAlert', blank=True, null=True)
    # Field name made lowercase.
    cntfeesalert = models.IntegerField(
        db_column='CntFeesAlert', blank=True, null=True)
    # Field name made lowercase.
    cntstepup = models.IntegerField(
        db_column='CntStepUp', blank=True, null=True)
    # Field name made lowercase.
    cntproposals = models.IntegerField(
        db_column='CntProposals', blank=True, null=True)
    # Field name made lowercase.
    cnt12step = models.IntegerField(
        db_column='Cnt12Step', blank=True, null=True)
    # Field name made lowercase.
    cntnrd = models.IntegerField(db_column='CntNRD', blank=True, null=True)
    # Field name made lowercase.
    cntsessions = models.IntegerField(
        db_column='CntSessions', blank=True, null=True)
    # Field name made lowercase.
    cntobjectivesdue = models.IntegerField(
        db_column='CntObjectivesDue', blank=True, null=True)
    # Field name made lowercase.
    cntratingsdue = models.IntegerField(
        db_column='CntRatingsDue', blank=True, null=True)
    # Field name made lowercase.
    cntnotesdue = models.IntegerField(
        db_column='CntNotesDue', blank=True, null=True)
    # Field name made lowercase.
    cntcourtdates = models.IntegerField(
        db_column='CntCourtDates', blank=True, null=True)
    # Field name made lowercase.
    cntbilling = models.IntegerField(
        db_column='CntBilling', blank=True, null=True)
    # Field name made lowercase.
    cntpayments = models.IntegerField(
        db_column='CntPayments', blank=True, null=True)
    # Field name made lowercase.
    cnttxattendance = models.IntegerField(
        db_column='CntTxAttendance', blank=True, null=True)
    # Field name made lowercase.
    cntscreens = models.IntegerField(
        db_column='CntScreens', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dashboard'


class Debttype(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    debttype = models.CharField(
        db_column='DebtType', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    sort = models.CharField(
        db_column='Sort', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DebtType'


class Debts(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    debttype = models.CharField(
        db_column='DebtType', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    debtdate = models.DateTimeField(
        db_column='DebtDate', blank=True, null=True)
    # Field name made lowercase.
    debtamount = models.DecimalField(
        db_column='DebtAmount', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    debtbalance = models.DecimalField(
        db_column='DebtBalance', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    statuscode = models.CharField(
        db_column='StatusCode', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = False
        db_table = 'Debts'


class Demographics(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    createdate = models.DateField(
        db_column='CreateDate', blank=True, null=True)
    # Field name made lowercase.
    white_m = models.IntegerField(db_column='White_M', blank=True, null=True)
    # Field name made lowercase.
    white_f = models.IntegerField(db_column='White_F', blank=True, null=True)
    # Field name made lowercase.
    white_t = models.IntegerField(db_column='White_T', blank=True, null=True)
    # Field name made lowercase.
    amindianalaskan_m = models.IntegerField(
        db_column='AmIndianAlaskan_M', blank=True, null=True)
    # Field name made lowercase.
    amindianalaskan_f = models.IntegerField(
        db_column='AmIndianAlaskan_F', blank=True, null=True)
    # Field name made lowercase.
    amindianalaskan_t = models.IntegerField(
        db_column='AmIndianAlaskan_T', blank=True, null=True)
    # Field name made lowercase.
    asian_m = models.IntegerField(db_column='Asian_M', blank=True, null=True)
    # Field name made lowercase.
    asian_f = models.IntegerField(db_column='Asian_F', blank=True, null=True)
    # Field name made lowercase.
    asian_t = models.IntegerField(db_column='Asian_T', blank=True, null=True)
    # Field name made lowercase.
    black_m = models.IntegerField(db_column='Black_M', blank=True, null=True)
    # Field name made lowercase.
    black_f = models.IntegerField(db_column='Black_F', blank=True, null=True)
    # Field name made lowercase.
    black_t = models.IntegerField(db_column='Black_T', blank=True, null=True)
    # Field name made lowercase.
    hispanic_m = models.IntegerField(
        db_column='Hispanic_M', blank=True, null=True)
    # Field name made lowercase.
    hispanic_f = models.IntegerField(
        db_column='Hispanic_F', blank=True, null=True)
    # Field name made lowercase.
    hispanic_t = models.IntegerField(
        db_column='Hispanic_T', blank=True, null=True)
    # Field name made lowercase.
    mideast_m = models.IntegerField(
        db_column='MidEast_M', blank=True, null=True)
    # Field name made lowercase.
    mideast_f = models.IntegerField(
        db_column='MidEast_F', blank=True, null=True)
    # Field name made lowercase.
    mideast_t = models.IntegerField(
        db_column='MidEast_T', blank=True, null=True)
    # Field name made lowercase.
    hawaiian_m = models.IntegerField(
        db_column='Hawaiian_M', blank=True, null=True)
    # Field name made lowercase.
    hawaiian_f = models.IntegerField(
        db_column='Hawaiian_F', blank=True, null=True)
    # Field name made lowercase.
    hawaiian_t = models.IntegerField(
        db_column='Hawaiian_T', blank=True, null=True)
    # Field name made lowercase.
    other_m = models.IntegerField(db_column='Other_M', blank=True, null=True)
    # Field name made lowercase.
    other_f = models.IntegerField(db_column='Other_F', blank=True, null=True)
    # Field name made lowercase.
    other_t = models.IntegerField(db_column='Other_T', blank=True, null=True)
    # Field name made lowercase.
    twoormore_m = models.IntegerField(
        db_column='TwoOrMore_M', blank=True, null=True)
    # Field name made lowercase.
    twoormore_f = models.IntegerField(
        db_column='TwoOrMore_F', blank=True, null=True)
    # Field name made lowercase.
    twoormore_t = models.IntegerField(
        db_column='TwoOrMore_T', blank=True, null=True)
    # Field name made lowercase.
    elementary = models.IntegerField(
        db_column='Elementary', blank=True, null=True)
    # Field name made lowercase.
    middleschool = models.IntegerField(
        db_column='MiddleSchool', blank=True, null=True)
    # Field name made lowercase.
    somehighschool = models.IntegerField(
        db_column='SomeHighSchool', blank=True, null=True)
    # Field name made lowercase.
    highschoolged = models.IntegerField(
        db_column='HighSchoolGED', blank=True, null=True)
    # Field name made lowercase.
    somecollege = models.IntegerField(
        db_column='SomeCollege', blank=True, null=True)
    # Field name made lowercase.
    associate = models.IntegerField(
        db_column='Associate', blank=True, null=True)
    # Field name made lowercase.
    bachelor = models.IntegerField(db_column='Bachelor', blank=True, null=True)
    # Field name made lowercase.
    graduate = models.IntegerField(db_column='Graduate', blank=True, null=True)
    # Field name made lowercase.
    lep = models.IntegerField(db_column='LEP', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_11andunder_m = models.IntegerField(
        db_column='11andUnder_M', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_11andunder_f = models.IntegerField(
        db_column='11andUnder_F', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_11andunder_t = models.IntegerField(
        db_column='11andUnder_T', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_12to17_m = models.IntegerField(
        db_column='12to17_M', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_12to17_f = models.IntegerField(
        db_column='12to17_F', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_12to17_t = models.IntegerField(
        db_column='12to17_T', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_18to20_m = models.IntegerField(
        db_column='18to20_M', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_18to20_f = models.IntegerField(
        db_column='18to20_F', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_18to20_t = models.IntegerField(
        db_column='18to20_T', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_21to25_m = models.IntegerField(
        db_column='21to25_M', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_21to25_f = models.IntegerField(
        db_column='21to25_F', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_21to25_t = models.IntegerField(
        db_column='21to25_T', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_26to35_m = models.IntegerField(
        db_column='26to35_M', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_26to35_f = models.IntegerField(
        db_column='26to35_F', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_26to35_t = models.IntegerField(
        db_column='26to35_T', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_36to45_m = models.IntegerField(
        db_column='36to45_M', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_36to45_f = models.IntegerField(
        db_column='36to45_F', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_36to45_t = models.IntegerField(
        db_column='36to45_T', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_46to55_m = models.IntegerField(
        db_column='46to55_M', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_46to55_f = models.IntegerField(
        db_column='46to55_F', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_46to55_t = models.IntegerField(
        db_column='46to55_T', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_56to65_m = models.IntegerField(
        db_column='56to65_M', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_56to65_f = models.IntegerField(
        db_column='56to65_F', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_56to65_t = models.IntegerField(
        db_column='56to65_T', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_66orolder_m = models.IntegerField(
        db_column='66orOlder_M', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_66orolder_f = models.IntegerField(
        db_column='66orOlder_F', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_66orolder_t = models.IntegerField(
        db_column='66orOlder_T', blank=True, null=True)
    # Field name made lowercase.
    gradunandem = models.IntegerField(
        db_column='GradUnandEm', blank=True, null=True)
    # Field name made lowercase.
    gradunandun = models.IntegerField(
        db_column='GradUnandUn', blank=True, null=True)
    # Field name made lowercase.
    grademandun = models.IntegerField(
        db_column='GradEmandUn', blank=True, null=True)
    # Field name made lowercase.
    grademandem = models.IntegerField(
        db_column='GradEmandEm', blank=True, null=True)
    # Field name made lowercase.
    married = models.IntegerField(db_column='Married', blank=True, null=True)
    # Field name made lowercase.
    commonlaw = models.IntegerField(
        db_column='CommonLaw', blank=True, null=True)
    # Field name made lowercase.
    separated = models.IntegerField(
        db_column='Separated', blank=True, null=True)
    # Field name made lowercase.
    divorced = models.IntegerField(db_column='Divorced', blank=True, null=True)
    # Field name made lowercase.
    widowed = models.IntegerField(db_column='Widowed', blank=True, null=True)
    # Field name made lowercase.
    single = models.IntegerField(db_column='Single', blank=True, null=True)
    # Field name made lowercase.
    noincome = models.IntegerField(db_column='NoIncome', blank=True, null=True)
    # Field name made lowercase.
    under999 = models.IntegerField(db_column='Under999', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1kto4999 = models.IntegerField(
        db_column='1Kto4999', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5kto9999 = models.IntegerField(
        db_column='5Kto9999', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_15kto19999 = models.IntegerField(
        db_column='15Kto19999', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_20kto34999 = models.IntegerField(
        db_column='20Kto34999', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_35kto44999 = models.IntegerField(
        db_column='35Kto44999', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_45kto54999 = models.IntegerField(
        db_column='45Kto54999', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_55kto64999 = models.IntegerField(
        db_column='55Kto64999', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_65kto74999 = models.IntegerField(
        db_column='65Kto74999', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_75korhigher = models.IntegerField(
        db_column='75KorHigher', blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    datastart = models.DateTimeField(
        db_column='DataStart', blank=True, null=True)
    # Field name made lowercase.
    dataend = models.DateTimeField(db_column='DataEnd', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_10kto14999 = models.IntegerField(
        db_column='10Kto14999', blank=True, null=True)
    # Field name made lowercase.
    totalactive = models.IntegerField(
        db_column='TotalActive', blank=True, null=True)
    # Field name made lowercase.
    totalgrads = models.IntegerField(
        db_column='TotalGrads', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Demographics'


class Disciplines(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    discipline = models.CharField(
        db_column='Discipline', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Disciplines'


class Drugtypes(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    drugtype = models.CharField(db_column='DrugType', max_length=50)

    class Meta:
        managed = False
        db_table = 'DrugTypes'


class Educationlevel(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    level = models.CharField(db_column='Level', max_length=50)

    class Meta:
        managed = False
        db_table = 'EducationLevel'


class Employment(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    occupation = models.CharField(
        db_column='Occupation', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    employer = models.CharField(db_column='Employer', max_length=50)
    # Field name made lowercase.
    contact = models.CharField(
        db_column='Contact', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    address = models.CharField(
        db_column='Address', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    city = models.CharField(
        db_column='City', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    state = models.CharField(
        db_column='State', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    zip = models.CharField(
        db_column='Zip', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    phone = models.CharField(
        db_column='Phone', max_length=12, blank=True, null=True)
    doh = models.DateTimeField(db_column='DOH')  # Field name made lowercase.
    # Field name made lowercase.
    dot = models.DateTimeField(db_column='DOT', blank=True, null=True)
    # Field name made lowercase.
    income = models.DecimalField(
        db_column='Income', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    hours = models.CharField(
        db_column='Hours', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    schedule = models.CharField(
        db_column='Schedule', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    payperiod = models.CharField(
        db_column='PayPeriod', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Employment'


class Fees(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(
        db_column='ClientID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    amount = models.DecimalField(
        db_column='Amount', max_digits=19, decimal_places=4)
    # Field name made lowercase.
    transdate = models.DateField(db_column='TransDate')
    # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=50)
    # Field name made lowercase.
    submitted = models.BooleanField(
        db_column='Submitted', blank=True, null=True)
    # Field name made lowercase.
    submitdate = models.DateField(
        db_column='SubmitDate', blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = False
        db_table = 'Fees'


class Frequency(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    frequency = models.CharField(
        db_column='Frequency', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Frequency'


class Gacounty(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    countyname = models.CharField(
        db_column='CountyName', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GACounty'


class Geninfo(models.Model):
    # Field name made lowercase.
    activeparticipants = models.IntegerField(
        db_column='ActiveParticipants', blank=True, null=True)
    # Field name made lowercase.
    reviewed = models.IntegerField(db_column='Reviewed', blank=True, null=True)
    # Field name made lowercase.
    rejectedprior = models.IntegerField(
        db_column='RejectedPrior', blank=True, null=True)
    # Field name made lowercase.
    declined = models.IntegerField(db_column='Declined', blank=True, null=True)
    # Field name made lowercase.
    acceptedprepost = models.IntegerField(
        db_column='AcceptedPrePost', blank=True, null=True)
    # Field name made lowercase.
    rejected2 = models.IntegerField(
        db_column='Rejected2', blank=True, null=True)
    # Field name made lowercase.
    rejected3 = models.IntegerField(
        db_column='Rejected3', blank=True, null=True)
    # Field name made lowercase.
    rejected4 = models.IntegerField(
        db_column='Rejected4', blank=True, null=True)
    # Field name made lowercase.
    county1 = models.IntegerField(db_column='County1', blank=True, null=True)
    # Field name made lowercase.
    county2 = models.IntegerField(db_column='County2', blank=True, null=True)
    # Field name made lowercase.
    county3 = models.IntegerField(db_column='County3', blank=True, null=True)
    # Field name made lowercase.
    county4 = models.IntegerField(db_column='County4', blank=True, null=True)
    # Field name made lowercase.
    county5 = models.IntegerField(db_column='County5', blank=True, null=True)
    # Field name made lowercase.
    county6 = models.IntegerField(db_column='County6', blank=True, null=True)
    # Field name made lowercase.
    county7 = models.IntegerField(db_column='County7', blank=True, null=True)
    # Field name made lowercase.
    county8 = models.IntegerField(db_column='County8', blank=True, null=True)
    # Field name made lowercase.
    county9 = models.IntegerField(db_column='County9', blank=True, null=True)
    # Field name made lowercase.
    county10 = models.IntegerField(db_column='County10', blank=True, null=True)
    # Field name made lowercase.
    cty1name = models.CharField(
        db_column='Cty1Name', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cty2name = models.CharField(
        db_column='Cty2Name', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cty3name = models.CharField(
        db_column='Cty3Name', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cty4name = models.CharField(
        db_column='Cty4Name', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cty5name = models.CharField(
        db_column='Cty5Name', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cty6name = models.CharField(
        db_column='Cty6Name', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cty7name = models.CharField(
        db_column='Cty7Name', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cty8name = models.CharField(
        db_column='Cty8Name', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cty9name = models.CharField(
        db_column='Cty9Name', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cty10name = models.CharField(
        db_column='Cty10Name', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    termadmindischarge = models.IntegerField(
        db_column='TermAdminDischarge', blank=True, null=True)
    # Field name made lowercase.
    termnoncompliance = models.IntegerField(
        db_column='TermNonCompliance', blank=True, null=True)
    # Field name made lowercase.
    termdismissed = models.IntegerField(
        db_column='TermDismissed', blank=True, null=True)
    # Field name made lowercase.
    screensbreath = models.IntegerField(
        db_column='ScreensBreath', blank=True, null=True)
    # Field name made lowercase.
    screenshair = models.IntegerField(
        db_column='ScreensHair', blank=True, null=True)
    # Field name made lowercase.
    screensurine = models.IntegerField(
        db_column='ScreensUrine', blank=True, null=True)
    # Field name made lowercase.
    screenstotal = models.IntegerField(
        db_column='ScreensTotal', blank=True, null=True)
    # Field name made lowercase.
    posscreens = models.IntegerField(
        db_column='PosScreens', blank=True, null=True)
    # Field name made lowercase.
    posscreensadmit = models.IntegerField(
        db_column='PosScreensAdmit', blank=True, null=True)
    # Field name made lowercase.
    posscreensdiluted = models.IntegerField(
        db_column='PosScreensDiluted', blank=True, null=True)
    # Field name made lowercase.
    posscreensnoshow = models.IntegerField(
        db_column='PosScreensNoShow', blank=True, null=True)
    # Field name made lowercase.
    posscreensnosample = models.IntegerField(
        db_column='PosScreensNoSample', blank=True, null=True)
    # Field name made lowercase.
    posscreensrefusal = models.IntegerField(
        db_column='PosScreensRefusal', blank=True, null=True)
    # Field name made lowercase.
    residentialtreatment = models.IntegerField(
        db_column='ResidentialTreatment', blank=True, null=True)
    # Field name made lowercase.
    substanceabusers = models.IntegerField(
        db_column='SubstanceAbusers', blank=True, null=True)
    # Field name made lowercase.
    sa_alcohol = models.IntegerField(
        db_column='SA_Alcohol', blank=True, null=True)
    # Field name made lowercase.
    sa_crack = models.IntegerField(db_column='SA_Crack', blank=True, null=True)
    # Field name made lowercase.
    sa_ecstasy = models.IntegerField(
        db_column='SA_Ecstasy', blank=True, null=True)
    # Field name made lowercase.
    sa_heroin = models.IntegerField(
        db_column='SA_Heroin', blank=True, null=True)
    # Field name made lowercase.
    sa_hallucin = models.IntegerField(
        db_column='SA_Hallucin', blank=True, null=True)
    # Field name made lowercase.
    sa_inhalants = models.IntegerField(
        db_column='SA_Inhalants', blank=True, null=True)
    # Field name made lowercase.
    sa_marijuana = models.IntegerField(
        db_column='SA_Marijuana', blank=True, null=True)
    # Field name made lowercase.
    sa_meth = models.IntegerField(db_column='SA_Meth', blank=True, null=True)
    # Field name made lowercase.
    sa_prescriptionnarc = models.IntegerField(
        db_column='SA_PrescriptionNarc', blank=True, null=True)
    # Field name made lowercase.
    sa_prescriptionother = models.IntegerField(
        db_column='SA_PrescriptionOther', blank=True, null=True)
    # Field name made lowercase.
    sa_other1 = models.IntegerField(
        db_column='SA_Other1', blank=True, null=True)
    # Field name made lowercase.
    sa_other2 = models.IntegerField(
        db_column='SA_Other2', blank=True, null=True)
    # Field name made lowercase.
    substanceusers = models.IntegerField(
        db_column='SubstanceUsers', blank=True, null=True)
    # Field name made lowercase.
    su_alcohol = models.IntegerField(
        db_column='SU_Alcohol', blank=True, null=True)
    # Field name made lowercase.
    su_crack = models.IntegerField(db_column='SU_Crack', blank=True, null=True)
    # Field name made lowercase.
    su_ecstasy = models.IntegerField(
        db_column='SU_Ecstasy', blank=True, null=True)
    # Field name made lowercase.
    su_heroin = models.IntegerField(
        db_column='SU_Heroin', blank=True, null=True)
    # Field name made lowercase.
    su_hallucin = models.IntegerField(
        db_column='SU_Hallucin', blank=True, null=True)
    # Field name made lowercase.
    su_inhalants = models.IntegerField(
        db_column='SU_Inhalants', blank=True, null=True)
    # Field name made lowercase.
    su_marijuana = models.IntegerField(
        db_column='SU_Marijuana', blank=True, null=True)
    # Field name made lowercase.
    su_meth = models.IntegerField(db_column='SU_Meth', blank=True, null=True)
    # Field name made lowercase.
    su_prescriptionnarc = models.IntegerField(
        db_column='SU_PrescriptionNarc', blank=True, null=True)
    # Field name made lowercase.
    su_prescriptionother = models.IntegerField(
        db_column='SU_PrescriptionOther', blank=True, null=True)
    # Field name made lowercase.
    su_other1 = models.IntegerField(
        db_column='SU_Other1', blank=True, null=True)
    # Field name made lowercase.
    su_other2 = models.IntegerField(
        db_column='SU_Other2', blank=True, null=True)
    # Field name made lowercase.
    asam0_5 = models.IntegerField(db_column='ASAM0_5', blank=True, null=True)
    # Field name made lowercase.
    asam1 = models.IntegerField(db_column='ASAM1', blank=True, null=True)
    # Field name made lowercase.
    asam2 = models.IntegerField(db_column='ASAM2', blank=True, null=True)
    # Field name made lowercase.
    asam2_5 = models.IntegerField(db_column='ASAM2_5', blank=True, null=True)
    # Field name made lowercase.
    asam3 = models.IntegerField(db_column='ASAM3', blank=True, null=True)
    # Field name made lowercase.
    asam4 = models.IntegerField(db_column='ASAM4', blank=True, null=True)
    # Field name made lowercase.
    modrisk = models.IntegerField(db_column='ModRisk', blank=True, null=True)
    # Field name made lowercase.
    highrisk = models.IntegerField(db_column='HighRisk', blank=True, null=True)
    # Field name made lowercase.
    judstatushearings = models.IntegerField(
        db_column='JudStatusHearings', blank=True, null=True)
    # Field name made lowercase.
    phase1 = models.IntegerField(db_column='Phase1', blank=True, null=True)
    # Field name made lowercase.
    phase2 = models.IntegerField(db_column='Phase2', blank=True, null=True)
    # Field name made lowercase.
    phase3 = models.IntegerField(db_column='Phase3', blank=True, null=True)
    # Field name made lowercase.
    phase4 = models.IntegerField(db_column='Phase4', blank=True, null=True)
    # Field name made lowercase.
    phase5 = models.IntegerField(db_column='Phase5', blank=True, null=True)
    # Field name made lowercase.
    su_o1name = models.IntegerField(
        db_column='SU_O1Name', blank=True, null=True)
    # Field name made lowercase.
    su_o2name = models.IntegerField(
        db_column='SU_O2Name', blank=True, null=True)
    # Field name made lowercase.
    sa_o1name = models.IntegerField(
        db_column='SA_O1Name', blank=True, null=True)
    # Field name made lowercase.
    sa_o2name = models.IntegerField(
        db_column='SA_O2Name', blank=True, null=True)
    # Field name made lowercase.
    rejected1 = models.IntegerField(
        db_column='Rejected1', blank=True, null=True)
    # Field name made lowercase.
    graduated = models.IntegerField(
        db_column='Graduated', blank=True, null=True)
    # Field name made lowercase.
    datastart = models.DateField(db_column='DataStart', blank=True, null=True)
    # Field name made lowercase.
    dataend = models.DateField(db_column='DataEnd', blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    acceptedprobrev = models.IntegerField(
        db_column='AcceptedProbRev', blank=True, null=True)
    # Field name made lowercase.
    rejected1descrip = models.CharField(
        db_column='Rejected1Descrip', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    rejected2descrip = models.CharField(
        db_column='Rejected2Descrip', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    rejected3descrip = models.CharField(
        db_column='Rejected3Descrip', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    rejected4descrip = models.CharField(
        db_column='Rejected4Descrip', max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GenInfo'


class Housing(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    housingname = models.CharField(
        db_column='HousingName', max_length=75, blank=True, null=True)
    # Field name made lowercase.
    housingrentamount = models.DecimalField(
        db_column='HousingRentAmount', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    housingaddress1 = models.CharField(
        db_column='HousingAddress1', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    housingaddress2 = models.CharField(
        db_column='HousingAddress2', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    housingcitystatezip = models.CharField(
        db_column='HousingCityStateZip', max_length=50)

    class Meta:
        managed = False
        db_table = 'Housing'


class Incomeranges(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    incomerange = models.CharField(db_column='IncomeRange', max_length=50)

    class Meta:
        managed = False
        db_table = 'IncomeRanges'


class Judges(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    division = models.SmallIntegerField(db_column='Division')
    # Field name made lowercase.
    judgename = models.CharField(db_column='JudgeName', max_length=55)
    # Field name made lowercase.
    judgeemail = models.CharField(
        db_column='JudgeEmail', max_length=75, blank=True, null=True)
    # Field name made lowercase.
    assistantname = models.CharField(
        db_column='AssistantName', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    assistantemail = models.CharField(
        db_column='AssistantEmail', max_length=75, blank=True, null=True)
    # Field name made lowercase.
    phone = models.CharField(
        db_column='Phone', max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Judges'


class Lsitypes(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    lsitype = models.CharField(
        db_column='LSIType', max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LSITypes'


class Mhphysicians(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    mhphysicianname = models.CharField(
        db_column='MHPhysicianName', max_length=50)
    # Field name made lowercase.
    mhfacilityname = models.CharField(
        db_column='MHFacilityName', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    mhaddress = models.CharField(
        db_column='MHAddress', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    mhcity = models.CharField(db_column='MHCity', max_length=25)
    # Field name made lowercase.
    mhstate = models.CharField(db_column='MHState', max_length=2)
    # Field name made lowercase.
    mhzip = models.CharField(
        db_column='MHZip', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    mhphone = models.CharField(
        db_column='MHPhone', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    mhpdate = models.DateTimeField(db_column='MHPDate', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MHPhysicians'


class Mentalhealth(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    evaldate = models.DateTimeField(
        db_column='EvalDate', blank=True, null=True)
    # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)
    # Field name made lowercase.
    medications = models.CharField(
        db_column='Medications', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = False
        db_table = 'MentalHealth'


class Objectives(models.Model):
    # Field name made lowercase.
    objid = models.AutoField(db_column='ObjID', primary_key=True)
    # Field name made lowercase.
    clientobjnum = models.IntegerField(
        db_column='ClientObjNum', blank=True, null=True)
    # Field name made lowercase.
    probgoalid = models.ForeignKey(
        'Probgoals', models.DO_NOTHING, db_column='ProbGoalID', blank=True, null=True)
    # Field name made lowercase.
    clientid = models.CharField(
        db_column='ClientID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    obj = models.CharField(
        db_column='Obj', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    objtarget = models.DateTimeField(
        db_column='ObjTarget', blank=True, null=True)
    # Field name made lowercase.
    intervention1 = models.CharField(
        db_column='Intervention1', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    intervention2 = models.CharField(
        db_column='Intervention2', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    closed = models.BooleanField(db_column='Closed')
    met = models.BooleanField(db_column='Met')  # Field name made lowercase.
    # Field name made lowercase.
    metdate = models.DateTimeField(db_column='MetDate', blank=True, null=True)
    # Field name made lowercase.
    rating = models.CharField(
        db_column='Rating', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')
    # Field name made lowercase.
    objtype = models.CharField(
        db_column='ObjType', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Objectives'


class Outreach(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    outreachdate = models.CharField(db_column='OutreachDate', max_length=50)
    # Field name made lowercase.
    outreachhours = models.SmallIntegerField(db_column='OutreachHours')
    # Field name made lowercase.
    outreachdescription = models.CharField(
        db_column='OutreachDescription', max_length=50)
    # Field name made lowercase.
    outreachverifiedby = models.CharField(
        db_column='OutreachVerifiedBy', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    type = models.CharField(
        db_column='Type', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Outreach'


class Phases(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    phase = models.CharField(db_column='Phase', max_length=10)
    # Field name made lowercase.
    track = models.CharField(
        db_column='Track', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    site = models.CharField(
        db_column='Site', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    screensperweek = models.IntegerField(
        db_column='ScreensPerWeek', blank=True, null=True)
    # Field name made lowercase.
    stepsessionsperweek = models.IntegerField(
        db_column='StepSessionsPerWeek', blank=True, null=True)
    # Field name made lowercase.
    meetingsperweek = models.IntegerField(
        db_column='MeetingsPerWeek', blank=True, null=True)
    # Field name made lowercase.
    courtperiod = models.CharField(
        db_column='CourtPeriod', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    txsessionsperperiod = models.IntegerField(
        db_column='TxSessionsPerPeriod', blank=True, null=True)
    # Field name made lowercase.
    txsessionhrs = models.FloatField(
        db_column='TxSessionHrs', blank=True, null=True)
    # Field name made lowercase.
    step = models.IntegerField(db_column='Step', blank=True, null=True)
    # Field name made lowercase.
    other = models.IntegerField(db_column='Other', blank=True, null=True)
    # Field name made lowercase.
    minphasedays = models.IntegerField(
        db_column='MinPhaseDays', blank=True, null=True)
    # Field name made lowercase.
    casereviewfreq = models.CharField(
        db_column='CaseReviewFreq', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    weeklyfees = models.DecimalField(
        db_column='WeeklyFees', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    cumfees = models.DecimalField(
        db_column='CumFees', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    employmenthrs = models.IntegerField(
        db_column='EmploymentHrs', blank=True, null=True)
    # Field name made lowercase.
    courtdateday = models.IntegerField(
        db_column='CourtDateDay', blank=True, null=True)
    # Field name made lowercase.
    grpnotes = models.IntegerField(db_column='GrpNotes', blank=True, null=True)
    # Field name made lowercase.
    grpnotefreq = models.CharField(
        db_column='GrpNoteFreq', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    indsession = models.IntegerField(
        db_column='IndSession', blank=True, null=True)
    # Field name made lowercase.
    feebalancealert = models.DecimalField(
        db_column='FeeBalanceAlert', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    courtfreqency = models.CharField(
        db_column='CourtFreqency', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    minimumdays = models.IntegerField(
        db_column='MinimumDays', blank=True, null=True)
    # Field name made lowercase.
    casereview = models.CharField(
        db_column='CaseReview', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    fees = models.DecimalField(
        db_column='Fees', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = False
        db_table = 'Phases'


class Physicians(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    physicianname = models.CharField(
        db_column='PhysicianName', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    facilityname = models.CharField(
        db_column='FacilityName', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    physicianaddress = models.CharField(
        db_column='PhysicianAddress', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    physiciancity = models.CharField(
        db_column='PhysicianCity', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    physicianstate = models.CharField(
        db_column='PhysicianState', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    physicianzip = models.CharField(
        db_column='PhysicianZip', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    physicianphone = models.CharField(
        db_column='PhysicianPhone', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    physiciandates = models.CharField(
        db_column='PhysicianDates', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Physicians'


class Positivetypes(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50)
    # Field name made lowercase.
    column2 = models.CharField(
        db_column='Column2', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PositiveTypes'


class Priortx(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=30)
    # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30)
    # Field name made lowercase.
    provider = models.CharField(
        db_column='Provider', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    provideraddress = models.CharField(
        db_column='ProviderAddress', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    providercity = models.CharField(
        db_column='ProviderCity', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    providerstate = models.CharField(
        db_column='ProviderState', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    providerzip = models.CharField(
        db_column='ProviderZip', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    providerphone = models.CharField(
        db_column='ProviderPhone', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)
    # Field name made lowercase.
    outcome = models.CharField(
        db_column='Outcome', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    yearssober = models.IntegerField(
        db_column='YearsSober', blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PriorTx'


class Probgoals(models.Model):
    # Field name made lowercase.
    probgoalid = models.AutoField(db_column='ProbGoalID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    disciplineid = models.IntegerField(db_column='DisciplineID')
    # Field name made lowercase.
    probgoalnum = models.IntegerField(db_column='ProbGoalNum')
    # Field name made lowercase.
    prob = models.CharField(db_column='Prob', max_length=100)
    # Field name made lowercase.
    goal = models.CharField(db_column='Goal', max_length=150)
    # Field name made lowercase.
    probgoaltarget = models.DateTimeField(db_column='ProbGoalTarget')
    # Field name made lowercase.
    probgoaltype = models.CharField(db_column='ProbGoalType', max_length=15)
    # Field name made lowercase.
    probgoalstatus = models.CharField(
        db_column='ProbGoalStatus', max_length=20)
    # Field name made lowercase.
    resolveddate = models.DateTimeField(
        db_column='ResolvedDate', blank=True, null=True)
    # Field name made lowercase.
    deferreddate = models.DateTimeField(
        db_column='DeferredDate', blank=True, null=True)
    # Field name made lowercase.
    closeddate = models.DateTimeField(
        db_column='ClosedDate', blank=True, null=True)
    # Field name made lowercase.
    lsir = models.CharField(
        db_column='LSIR', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProbGoals'


class Proposals(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    proposaltype = models.CharField(db_column='ProposalType', max_length=15)
    # Field name made lowercase.
    proposaldate = models.DateField(db_column='ProposalDate')
    # Field name made lowercase.
    passstart = models.CharField(
        db_column='PassStart', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    passend = models.CharField(
        db_column='PassEnd', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    proposaldescription = models.CharField(
        db_column='ProposalDescription', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    proposalstatus = models.CharField(
        db_column='ProposalStatus', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    proposalcomment = models.CharField(
        db_column='ProposalComment', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    laststatusdate = models.DateField(
        db_column='LastStatusDate', blank=True, null=True)
    # Field name made lowercase.
    approver = models.CharField(
        db_column='Approver', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    approvedate = models.DateField(
        db_column='ApproveDate', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    passdate = models.DateField(db_column='Passdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Proposals'


class Race(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    racetitle = models.CharField(
        db_column='RaceTitle', max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Race'


class Ratinghistory(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    ratingdate = models.DateTimeField(
        db_column='RatingDate', blank=True, null=True)
    # Field name made lowercase.
    probgoalid = models.IntegerField(
        db_column='ProbGoalID', blank=True, null=True)
    # Field name made lowercase.
    objid = models.IntegerField(db_column='ObjID', blank=True, null=True)
    # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)
    # Field name made lowercase.
    description = models.CharField(
        db_column='Description', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    crating = models.CharField(
        db_column='CRating', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    prating = models.CharField(
        db_column='PRating', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    rater = models.CharField(
        db_column='Rater', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    problemid = models.IntegerField(
        db_column='ProblemID', blank=True, null=True)
    # Field name made lowercase.
    objectiveid = models.IntegerField(
        db_column='ObjectiveID', blank=True, null=True)
    # Field name made lowercase.
    currentphase = models.CharField(
        db_column='CurrentPhase', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    phasedays = models.IntegerField(
        db_column='PhaseDays', blank=True, null=True)
    # Field name made lowercase.
    nextratingdate = models.DateTimeField(
        db_column='NextRatingDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RatingHistory'


class Referrals(models.Model):
    # STATUS_CREATED = 0
    # STATUS_PRETRIAL = 1
    # STATUS_DEFENSE = 2
    # STATUS_DA = 3
    # STATUS_ASSESSMENT = 4
    # STATUS_TEAM = 5
    # STATUS_APPROVED = 6
    # STATUS_REJECTED = 7
    # STATUS_WAITING = 8

    # STATUS_CHOICES = (
    #     (STATUS_CREATED, 'created'),
    #     (STATUS_PRETRIAL, 'pretrial'),
    #     (STATUS_DEFENSE, 'defense'),
    #     (STATUS_DA, 'district_attorney'),
    #     (STATUS_ASSESSMENT, 'assessment'),
    #     (STATUS_TEAM, 'assessment'),
    #     (STATUS_APPROVED, 'approved'),
    #     (STATUS_REJECTED, 'rejected'),
    #     (STATUS_WAITING, 'waiting')
    # )

    # status = FSMField(choices=STATUS_CHOICES, default=STATUS_CREATED)

    # Field name made lowercase.
    refid = models.AutoField(db_column='RefID', primary_key=True)
    # Field name made lowercase.
    # autoincrement ClientID and refID
    clientid = models.CharField(
        db_column='ClientID', unique=True, max_length=15)
    # Field name made lowercase.
    casenums = models.CharField(
        db_column='CaseNums', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    charges = models.CharField(
        db_column='Charges', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    spn = models.CharField(db_column='SPN', max_length=8,
                           blank=True, null=True)
    # Field name made lowercase.
    stateid = models.CharField(
        db_column='StateID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    lastname = models.CharField(
        db_column='LastName', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    firstname = models.CharField(
        db_column='FirstName', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    middlename = models.CharField(
        db_column='MiddleName', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    ssn = models.CharField(
        db_column='SSN', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    track = models.CharField(db_column='Track', max_length=1)
    # Field name made lowercase.
    enrolldate = models.DateField(
        db_column='EnrollDate', blank=True, null=True)
    # Field name made lowercase.
    rejectreason = models.CharField(
        db_column='RejectReason', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)
    # Field name made lowercase.
    race = models.CharField(
        db_column='Race', max_length=35, blank=True, null=True)
    # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1,
                           blank=True, null=True)
    # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)
    # Field name made lowercase.
    division = models.IntegerField(db_column='Division', blank=True, null=True)
    # Field name made lowercase.
    location = models.CharField(
        db_column='Location', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    cell = models.CharField(
        db_column='Cell', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    referredby = models.CharField(
        db_column='ReferredBy', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    referreddate = models.DateField(
        db_column='ReferredDate', blank=True, null=True)
    # Field name made lowercase.
    pretrialname = models.CharField(
        db_column='PretrialName', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    pretrialreceived = models.DateField(
        db_column='PretrialReceived', blank=True, null=True)
    # Field name made lowercase.
    pretrialcompleted = models.DateField(
        db_column='PretrialCompleted', blank=True, null=True)
    # Field name made lowercase.
    pretrialdecision = models.CharField(
        db_column='PretrialDecision', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    defensename = models.CharField(
        db_column='DefenseName', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    defensereceived = models.DateField(
        db_column='DefenseReceived', blank=True, null=True)
    # Field name made lowercase.
    defensecompleted = models.DateField(
        db_column='DefenseCompleted', blank=True, null=True)
    # Field name made lowercase.
    defensedecision = models.CharField(
        db_column='DefenseDecision', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    daname = models.CharField(
        db_column='DAName', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    dareceived = models.DateField(
        db_column='DAReceived', blank=True, null=True)
    # Field name made lowercase.
    dacompleted = models.DateField(
        db_column='DACompleted', blank=True, null=True)
    # Field name made lowercase.
    dadecision = models.CharField(
        db_column='DADecision', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    assessname = models.CharField(
        db_column='AssessName', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    assessreceived = models.DateField(
        db_column='AssessReceived', blank=True, null=True)
    # Field name made lowercase.
    assesscompleted = models.DateField(
        db_column='AssessCompleted', blank=True, null=True)
    # Field name made lowercase.
    teamreceived = models.DateField(
        db_column='TeamReceived', blank=True, null=True)
    # Field name made lowercase.
    teamcompleted = models.DateField(
        db_column='TeamCompleted', blank=True, null=True)
    # Field name made lowercase.
    teamdecision = models.CharField(
        db_column='TeamDecision', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    arrests = models.IntegerField(db_column='Arrests', blank=True, null=True)
    # Field name made lowercase.
    felonies = models.IntegerField(db_column='Felonies', blank=True, null=True)
    # Field name made lowercase.
    misdemeanors = models.IntegerField(
        db_column='Misdemeanors', blank=True, null=True)
    # Field name made lowercase.
    firstarrestyear = models.IntegerField(
        db_column='FirstArrestYear', blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    accepteddate = models.DateField(
        db_column='AcceptedDate', blank=True, null=True)
    # Field name made lowercase.
    county = models.CharField(
        db_column='County', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    type = models.CharField(
        db_column='Type', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    termreason = models.CharField(
        db_column='TermReason', max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Referrals'

    # @transition(field=status, source=STATUS_CREATED, target=STATUS_DA)
    # def client_created(self):
    #     # initial client form filled out
    #     if self.clientid:
    #         return

    # @transition(field=status,
    #     source=[STATUS_DA, STATUS_DEFENSE, STATUS_PRETRIAL, STATUS_TEAM],
    #     target=[STATUS_APPROVED, STATUS_REJECTED])
    # def client_review(self):
    #     pass
    #     # if all source statuses are TRUE:
    #     # Approved elif rejected else waiting
    
    def get_absolute_url(self):
        return reverse('referrals-update', kwargs={'pk': self.refid})

class Rejectreasons(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    rejectreason = models.CharField(
        db_column='RejectReason', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RejectReasons'


class Rewards(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    courtid = models.ForeignKey(
        Court, models.DO_NOTHING, db_column='CourtID', blank=True, null=True)
    # Field name made lowercase.
    rewarddate = models.DateTimeField(
        db_column='RewardDate', blank=True, null=True)
    # Field name made lowercase.
    rewarddescription = models.CharField(
        db_column='RewardDescription', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    clientid = models.CharField(
        db_column='ClientID', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rewards'


class Sanctionlevels(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    sanctionlevel = models.CharField(db_column='SanctionLevel', max_length=50)

    class Meta:
        managed = False
        db_table = 'SanctionLevels'


class Sanctions(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    sanctionlevel = models.CharField(db_column='SanctionLevel', max_length=50)
    # Field name made lowercase.
    sanctiondate = models.DateTimeField(
        db_column='SanctionDate', blank=True, null=True)
    # Field name made lowercase.
    description = models.CharField(
        db_column='Description', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    daysinjail = models.SmallIntegerField(
        db_column='DaysInJail', blank=True, null=True)
    # Field name made lowercase.
    datejailstart = models.DateTimeField(
        db_column='DateJailStart', blank=True, null=True)
    # Field name made lowercase.
    datejailend = models.DateTimeField(
        db_column='DateJailEnd', blank=True, null=True)
    # Field name made lowercase.
    csprovider = models.CharField(
        db_column='CSProvider', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    csdate = models.CharField(
        db_column='CSDate', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cshoursrequired = models.SmallIntegerField(
        db_column='CSHoursRequired', blank=True, null=True)
    # Field name made lowercase.
    cshourscompleted = models.SmallIntegerField(
        db_column='CSHoursCompleted', blank=True, null=True)
    # Field name made lowercase.
    csverifiedby = models.CharField(
        db_column='CSVerifiedBy', max_length=55, blank=True, null=True)
    # Field name made lowercase.
    complete = models.BooleanField(db_column='Complete', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    level4complete = models.BooleanField(db_column='Level4Complete')
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = False
        db_table = 'Sanctions'


class Screensimport(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    accession = models.IntegerField(
        db_column='Accession', blank=True, null=True)
    # Field name made lowercase.
    clientid = models.CharField(
        db_column='ClientID', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    collectdate = models.DateTimeField(
        db_column='CollectDate', blank=True, null=True)
    # Field name made lowercase.
    testdate = models.DateTimeField(
        db_column='TestDate', blank=True, null=True)
    # Field name made lowercase.
    result = models.CharField(
        db_column='Result', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    drugsfound = models.CharField(
        db_column='Drugsfound', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    notes = models.CharField(
        db_column='Notes', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    agency = models.CharField(
        db_column='Agency', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ScreensImport'


class Screenslab(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    agency = models.CharField(
        db_column='Agency', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    accession = models.IntegerField(db_column='Accession')
    # Field name made lowercase.
    collectdate = models.DateTimeField(
        db_column='CollectDate', blank=True, null=True)
    # Field name made lowercase.
    testdate = models.DateTimeField(
        db_column='TestDate', blank=True, null=True)
    # Field name made lowercase.
    result = models.CharField(
        db_column='Result', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    resultconfirmed = models.BooleanField(db_column='ResultConfirmed')
    # Field name made lowercase.
    positiveapproved = models.BooleanField(db_column='PositiveApproved')
    # Field name made lowercase.
    drugsfound = models.CharField(
        db_column='DrugsFound', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    notes = models.CharField(
        db_column='Notes', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')
    # Field name made lowercase.
    positivetype = models.CharField(
        db_column='PositiveType', max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ScreensLab'


class Screensother(models.Model):
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    collectdate = models.DateTimeField(db_column='CollectDate')
    # Field name made lowercase.
    result = models.CharField(
        db_column='Result', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    resultconfirmed = models.BooleanField(
        db_column='ResultConfirmed', blank=True, null=True)
    # Field name made lowercase.
    positiveapproved = models.BooleanField(db_column='PositiveApproved')
    # Field name made lowercase.
    noshow = models.BooleanField(db_column='NoShow')
    # Field name made lowercase.
    drugsfound = models.CharField(
        db_column='DrugsFound', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    notes = models.CharField(
        db_column='Notes', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')
    # Field name made lowercase.
    refusal = models.BooleanField(db_column='Refusal', blank=True, null=True)
    # Field name made lowercase.
    diluted = models.BooleanField(db_column='Diluted', blank=True, null=True)
    # Field name made lowercase.
    admitted = models.BooleanField(db_column='Admitted', blank=True, null=True)
    # Field name made lowercase.
    positivetype = models.CharField(
        db_column='PositiveType', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ScreensOther'


class Status(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    statusmsg = models.CharField(
        db_column='StatusMsg', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    msgtype = models.CharField(
        db_column='MsgType', max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Status'


class Stepattendance(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    weekstart = models.DateField(db_column='WeekStart', blank=True, null=True)
    # Field name made lowercase.
    attended = models.IntegerField(db_column='Attended', blank=True, null=True)
    # Field name made lowercase.
    comment = models.CharField(
        db_column='Comment', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    modified = models.DateTimeField(
        db_column='Modified', blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    required = models.IntegerField(db_column='Required', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StepAttendance'


class Substanceuse(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    aod = models.CharField(
        db_column='AOD', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    route = models.CharField(
        db_column='Route', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    frequency = models.CharField(
        db_column='Frequency', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    agebegan = models.IntegerField(db_column='AgeBegan', blank=True, null=True)
    # Field name made lowercase.
    lastuse = models.CharField(
        db_column='LastUse', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    comments = models.CharField(
        db_column='Comments', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    usebyfamily = models.BooleanField(db_column='UseByFamily')
    # Field name made lowercase.
    usebypartner = models.BooleanField(db_column='UseByPartner')
    # Field name made lowercase.
    currentlyused = models.BooleanField(db_column='CurrentlyUsed')
    # Field name made lowercase.
    costperweek = models.DecimalField(
        db_column='CostPerWeek', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = False
        db_table = 'SubstanceUse'


class Tempnote(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    tempnote = models.TextField(db_column='TempNote', blank=True, null=True)
    # Field name made lowercase.
    notedate = models.DateTimeField(
        db_column='NoteDate', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')
    # Field name made lowercase.
    createdate = models.DateTimeField(
        db_column='CreateDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TempNote'


class Temprating(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    ratingdate = models.DateTimeField(
        db_column='RatingDate', blank=True, null=True)
    # Field name made lowercase.
    probgoalid = models.IntegerField(db_column='ProbGoalID')
    # Field name made lowercase.
    objid = models.IntegerField(db_column='ObjID', blank=True, null=True)
    # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)
    # Field name made lowercase.
    description = models.CharField(
        db_column='Description', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    crating = models.CharField(
        db_column='CRating', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    prating = models.CharField(
        db_column='PRating', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    rater = models.CharField(
        db_column='Rater', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TempRating'


class Temptxattendance(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    name = models.CharField(
        db_column='Name', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    sessiondate = models.DateTimeField(
        db_column='SessionDate', blank=True, null=True)
    # Field name made lowercase.
    aaorna = models.BooleanField(db_column='AAorNA', blank=True, null=True)
    # Field name made lowercase.
    attendance = models.BooleanField(
        db_column='Attendance', blank=True, null=True)
    # Field name made lowercase.
    attendancecomments = models.CharField(
        db_column='AttendanceComments', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    reason = models.CharField(
        db_column='Reason', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    txid = models.IntegerField(db_column='TxID', blank=True, null=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    timein = models.CharField(
        db_column='TimeIn', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    timeout = models.CharField(
        db_column='Timeout', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = False
        db_table = 'TempTxAttendance'


class Temptxnotes(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    lfname = models.CharField(
        db_column='LFName', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)
    # Field name made lowercase.
    notetype = models.CharField(
        db_column='NoteType', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    notedate = models.DateTimeField(
        db_column='NoteDate', blank=True, null=True)
    # Field name made lowercase.
    probgoalnum = models.CharField(
        db_column='ProbGoalNum', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    timein = models.CharField(
        db_column='TimeIn', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    timeout = models.CharField(
        db_column='TimeOut', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    reason = models.CharField(
        db_column='Reason', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    nrd = models.DateTimeField(db_column='NRD', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = False
        db_table = 'TempTxNotes'


class Txattendance(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    # Field name made lowercase.
    sessiondate = models.DateTimeField(db_column='SessionDate')
    # Field name made lowercase.
    attendedyn = models.BooleanField(
        db_column='AttendedYN', blank=True, null=True)
    # Field name made lowercase.
    nonattendreason = models.CharField(
        db_column='NonAttendReason', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    timein = models.CharField(
        db_column='TimeIn', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    timeout = models.CharField(
        db_column='TimeOut', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = False
        db_table = 'TxAttendance'


class Txnotes(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=15)
    note = models.TextField(db_column='Note')  # Field name made lowercase.
    # Field name made lowercase.
    notetype = models.CharField(db_column='NoteType', max_length=15)
    # Field name made lowercase.
    notedate = models.DateTimeField(db_column='NoteDate')
    # Field name made lowercase.
    probgoalnum = models.CharField(
        db_column='ProbGoalNum', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    timein = models.CharField(
        db_column='TimeIn', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    timeout = models.CharField(
        db_column='TimeOut', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    reason = models.CharField(
        db_column='Reason', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    nrd = models.DateTimeField(db_column='NRD', blank=True, null=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')
    # Field name made lowercase.
    notetoclient = models.TextField(
        db_column='NoteToClient', blank=True, null=True)
    # Field name made lowercase.
    phase = models.CharField(
        db_column='Phase', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    discipline = models.CharField(
        db_column='Discipline', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TxNotes'


class Userinfo(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=25)
    # Field name made lowercase.
    username = models.CharField(
        db_column='UserName', max_length=55, blank=True, null=True)
    # Field name made lowercase.
    roleid = models.IntegerField(db_column='RoleID')
    # Field name made lowercase.
    useremail = models.CharField(
        db_column='UserEmail', max_length=75, blank=True, null=True)
    # Field name made lowercase.
    userphone = models.CharField(
        db_column='UserPhone', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)
    # Field name made lowercase.
    defaulttrack = models.CharField(
        db_column='DefaultTrack', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')

    class Meta:
        managed = False
        db_table = 'UserInfo'


class Userlogininfo(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    startsession = models.DateTimeField(
        db_column='StartSession', blank=True, null=True)
    # Field name made lowercase.
    finishsession = models.DateTimeField(
        db_column='FinishSession', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserLoginInfo'
