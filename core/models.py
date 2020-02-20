from django.db import models

# Create your models here.
class medicalhistory(TimeStampedModel):
    NeedleUse = models.BooleanField
    FamilyofOriginYN = models.BooleanField
    FamilyofOriginUse = models.CharField(max_length=250
    SpouseUseYN = models.BooleanField
    SpouseUseComment = models.CharField(max_length=250)
    TestType = models.CharField(max_length=50)
    TestResults = models.CharField(max_length=250)
    SubstanceUse = models.CharField(max_length=250)
    Sobriety = models.CharField(max_length=50)
    PrimaryDrug = models.CharField(max_length=250
    LastPositive
    Diagnosis = models.CharField(max_length=250)
    Suicide = models.BooleanField
    Violence = models.BooleanField
    Health = models.CharField(max_length=250)
    GhMedications = models.CharField(max_length=250)
    Prenatal = models.CharField(max_length=250)
    TBStatus = models.CharField(max_length=250)
    PhysicalAbuse = models.BooleanField
    SexualAbuse = models.BooleanField
    InsuranceYN = models.BooleanField
    Insurance =  = models.CharField(max_length=250)
    AddictionSeverityIndex = models.CharField(max_length=50)
    LEP = models.BooleanField
    ASAM_LOC = models.CharField(max_length=250)
    OutcomeComments =  = models.CharField(max_length=250)

class ClientInfo(TimeStampedModel):
    CellPhone = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Message = models.CharField(max_length=50)
    MessageSource = models.CharField(max_length=50)
    IncomeSource = models.CharField(max_length=50)
    YearlyIncome = models.IntegerField()
    EducationYrs = models.CharField(max_length=50)
    EducationLevel = models.CharField(max_length=50)
    HighSchoolGrad = models.CharField(max_length=50)
    GED = models.CharField(max_length=50)
    MilitaryService= models.BooleanField
    VAEligible= models.BooleanField
    MaritalStatus = models.CharField(max_length=50)
    Pregnant= models.BooleanField
    Children= models.BooleanField
    ChildNarrative = models.CharField(max_length=50)
    EmployedAtStart = models.CharField(max_length=50)
    EmployedAtGrad = models.CharField(max_length=50)
