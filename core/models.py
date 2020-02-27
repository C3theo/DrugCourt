from django.db import models
from model_utils.models import TimeStampedModel



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
