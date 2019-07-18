from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from model_utils import Choices

from guardian.mixins import GuardianUserMixin


class BaseProfile(models.Model):

    USER_ROLES = Choices('Drug Court Team', 'DA', 'Defense',
                         'Pretrial', 'Screener', 'Developer')

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    user_role = models.CharField('User Role', max_length=20,
                                 null=True, blank=True, choices=USER_ROLES)

    def __str__(self):
        return f"{self.user} - Role:{self.get_user_role_display()}"

    class Meta:
        abstract = True

# TODO: future profiles - court etc
# TODO: add to group based off user_role?


class DrugCourtProfile(models.Model):
    # TODO: make Foreign Key Field
    # division = models.CharField(max_length=20)

    class Meta:
        abstract = True


class DAProfile(models.Model):
    pass

    class Meta:
        abstract = True


class DefenseProfile(models.Model):
    pass

    class Meta:
        abstract = True


class Profile(GuardianUserMixin, DrugCourtProfile, BaseProfile):
    pass

    class Meta:
        verbose_name = 'profile'
