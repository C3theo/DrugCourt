from django.db import models
from intake.models import Client
from model_utils import Choices
from model_utils.models import TimeStampedModel


class ProbGoalStatusOptions:

    Active = 'Active'
    Maintenance = 'Maintenance'
    Referred = 'Referred'
    ReferredToCaseMgmt = 'Referred to Case Mgmt'
    Deferred = 'Deferred'
    Resolved = 'Resolved'
    Refused = 'Refused'

    CHOICES = Choices(Active, Maintenance, Referred,
                      ReferredToCaseMgmt, Deferred, Resolved, Refused)


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

    CHOICES = Choices(zero, one, two, three)


class Objectives(TimeStampedModel):
    """
    """
    client = models.ForeignKey(
        'intake.client', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=250)
    obj_num = models.IntegerField()
    obj_target = models.DateField()
    closed = models.BooleanField()
    met = models.BooleanField()
    met_date = models.DateField(blank=True, null=True)
    tx_rating = models.IntegerField(blank=True, null=True)
    client_rating = models.IntegerField(blank=True, null=True)

    # def meta(self):
    #     return self.meta


class ProbGoals(TimeStampedModel):
    """
    """
    client = models.ForeignKey(
        'intake.client', on_delete=models.CASCADE, blank=True, null=True)
    objective = models.ForeignKey(
        'objectives', related_name='goals',
        on_delete=models.CASCADE, blank=True, null=True)
    prob_description = models.TextField(max_length=250)
    goal_description = models.TextField(max_length=250)
    prob_goal_num = models.IntegerField()
    prob_goal_target = models.DateField()
    prob_goal_status = models.CharField(
        max_length=25, choices=ProbGoalStatusOptions.CHOICES)
    status_date = models.DateField(blank=True, null=True)


class TxAttendance(TimeStampedModel):
    """
    """
    client = models.ForeignKey(
        'intake.client', on_delete=models.CASCADE, blank=True, null=True)
    session_date = models.DateField()
    attended = models.BooleanField()
    absence_reason = models.CharField(
        max_length=25, choices=AbsenceReasons.CHOICES)
    time_in = models.TimeField()
    time_out = models.TimeField()


class TxProgress(TimeStampedModel):
    """
    """
    client = models.ForeignKey(
        'intake.client', on_delete=models.CASCADE, blank=True, null=True)
    note = models.ForeignKey(
        'intake.Note', on_delete=models.CASCADE, null=True, blank=True)
    time_in = models.TimeField()
    time_out = models.TimeField()
    problems = models.TextField(max_length=250)
    next_review = models.DateField()


class Ratings(TimeStampedModel):
    """
    """
    client = models.ForeignKey(
        'intake.client', on_delete=models.CASCADE, blank=True, null=True)
    rating_date = models.DateField()
    prob_goal = models.ForeignKey(
        'ProbGoals', on_delete=models.CASCADE, blank=True, null=True)
    obj_id = models.ForeignKey(
        'objectives', on_delete=models.CASCADE, blank=True, null=True)
    item_description = models.TextField(max_length=250)
    staff_rating = models.CharField(max_length=1, choices=RatingChoice.CHOICES)
    client_rating = models.CharField(
        max_length=1, choices=RatingChoice.CHOICES)
    client_obj_number = models.IntegerField()
