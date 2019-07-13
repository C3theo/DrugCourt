from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from guardian.mixins import GuardianUserMixin

# This is for when subclassing AbstractUser
# def get_anonymous_user_instance(User):
#     return User(user_role=None)

class BaseProfile(models.Model):

    USER_ROLES = (
        (0, 'Drug Court Team'),
        (1, 'DA'),
        (2, 'Defense'),
        (3, 'Pretrial'),
        (4, 'Screener'),
        (5, 'Developer'),)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    user_role = models.IntegerField('User Role',
                                    null=True, choices=USER_ROLES, default=0)

    def __str__(self):
        return f"{self.user} - {self.get_user_role_display()}"

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
