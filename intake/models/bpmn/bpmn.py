from viewflow import flow
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from django.db import models
from viewflow.models import Process

# ConcurrentTransitionMixin, models.Model
from profiles.models import Profile


class DynamicSplitProcess(Process):
    question = models.CharField(max_length=50)
    split_count = models.IntegerField(default=0)


class Decision(models.Model):
    """
        Model to represent decisions about client eligibility.
    """

    user = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    date_received = models.DateTimeField()
    date_completed = models.DateTimeField()
    verdict = models.BooleanField(default=False)
    # verdict = FSMField('Verdict', choices=STATUS_CHOICES,
    #                    max_length=20, default=0)
    referral = models.ForeignKey(
        'intake.Referral', on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     pass

    # class Meta:
    #     managed = True
    #     permissions = [('can_decide', 'Can Decide')
    #                    ]

    # def one_decision_per_group(self, role):
    #     """
    #         FSM transition to check whether a decision from user's group has
    #         already been made.
    #     """
    #     # role = self.user.user_role
    #     decisions = Decision.objects.filter(
    #         referral=self.referral, user__user_role=role)

    #     return len(decisions.values_list()) == 1
    #     # When this condition needs to be checked a user has not made decision (return value makes no sense)
    #     # seems like it should go with Referral status, but it does not have a user attribute (needed to check user role)
    #     # Needs to be passed in from view function

    # @transition(field=verdict, source=STATUS_PENDING, target=STATUS_APPROVED,
    #             conditions=[one_decision_per_group], permission=lambda instance, user: user.has_perm('can_decide'))
    # def approve(self):
    #     pass


def check_user_role_not_assigned(self, user_role):
    """
        Return whether another user with same role
        is already working on this decision.
    """
    # check object assigned error
    raise(NotImplementedError)


class Phase(models.Model):
    """
    """
    CHOICES = ((0, 'Not in System'),
                     (1, 'Phase One'),
                     (2, 'Phase Two'),
                     (3, 'Phase Three'),)

    phase_id = models.CharField(
        max_length=20, choices=CHOICES, null=True, blank=True)
    screens_per_week = models.IntegerField(default=1)
    meetings_per_week = models.IntegerField(default=1)
    fees = models.CharField(max_length=4, null=True, blank=True, default='20')
    notes = models.ForeignKey('intake.Note', null=True,
                              blank=True, on_delete=models.CASCADE)
    review_frequency = models.IntegerField(default=1)


class HelloWorldProcess(Process):
    text = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)