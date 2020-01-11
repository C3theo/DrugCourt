from django.db import models
from intake.models import Client
from model_utils import Choices
from model_utils.models import TimeStampedModel 

# Create your models here.
class ProbGoalStatusOptions:

    Active = 'Active'
    Maintenance = 'Maintenance'
    Referred = 'Referred'
    ReferredToCaseMgmt = 'Referred to Case Mgmt'
    Deferred = 'Deferred'
    Resolved = 'Resolved'
    Refused = 'Refused'

    CHOICES = Choices(Active, Maintenance, Referred, ReferredToCaseMgmt, Deferred, Resolved, Refused)

class AbsenceReasons:

    Absent = 'Absent'
    Late = 'Late'
    Excused = 'Excused'
    Medical = 'Medical'

    CHOICES = Choices(Absent, Late, Excused, Medical)

class TxNoteTypes:

    Individual = 'Individual'
    Group = 'Group'
    Staffing = 'Staffing'
    Contact = 'Contact'

    CHOICES = Choices(Individual, Group, Staffing, Contact)

class RatingChoice:

    zero = '0'
    one = '1'
    two = '2'
    three = '3'

    CHOICES = Choices(zero,one,two,three)


class Objectives(TimeStampedModel):
    client_id = models.ForeignKey(
        'intake.client', on_delete=models.CASCADE, blank=True, null=True)
    ObjDescrip = models.TextField(max_length=250)
    ClientObjNum = models.IntegerField
    ObjTarget = models.DateField
    Closed = models.BooleanField
    Met = models.BooleanField
    MetDate = models.DateField
    TxRating = models.IntegerField
    ClientRating = models.IntegerField

class ProbGoals(TimeStampedModel):
    client_id = models.ForeignKey(
        'intake.client', on_delete=models.CASCADE, blank=True, null=True)
    Obj_id = models.ForeignKey(
        'objectives', on_delete=models.CASCADE, blank=True, null=True)
    ProbDescrip = models.TextField(max_length=250)
    GoalDescrip = models.TextField(max_length=250)
    ClientProbGoalNum = models.IntegerField
    ProGoalTarget = models.DateField
    ProbGoalStatus = models.CharField(max_length=1, choices=ProbGoalStatusOptions.CHOICES)
    StatusDate = models.DateField

class TxAttendance(TimeStampedModel):
    client_id = models.ForeignKey(
        'intake.client', on_delete=models.CASCADE, blank=True, null=True)
    SessionDate = models.DateField
    Attended = models.BooleanField
    AbsenceReason = models.CharField(max_length=1, choices=AbsenceReasons.CHOICES)
    TimeIn = models.TimeField
    TimeOut = models.TimeField

class TxProgress(TimeStampedModel):
    client_id = models.ForeignKey(
        'intake.client', on_delete=models.CASCADE, blank=True, null=True)
    NoteType = models.CharField(max_length=1, choices=TxNoteTypes.CHOICES)
    TimeIn = models.TimeField
    TimeOut = models.TimeField
    Problems = models.TextField(max_length=250)
    NextReview = models.DateField

class Ratings(TimeStampedModel):
    client_id = models.ForeignKey(
        'intake.client', on_delete=models.CASCADE, blank=True, null=True)
    RatingDate = models.DateField
    ProbGoalID = models.ForeignKey(
        'ProbGoals', on_delete=models.CASCADE, blank=True, null=True)
    ObjID = models.ForeignKey(
        'objectives', on_delete=models.CASCADE, blank=True, null=True)
    ItemDescription = models.TextField(max_length=250)
    StaffRating = models.CharField(max_length=1, choices=RatingChoice.CHOICES)
    ClientRating = models.CharField(max_length=1, choices=RatingChoice.CHOICES)
    ClientObjNumber = models.IntegerField
