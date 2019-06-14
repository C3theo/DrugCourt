from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from guardian.shortcuts import assign_perm
from . import models


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender, instance, created, **kwargs):

   
    if created and instance.username != settings.ANONYMOUS_USER_NAME:
        profile = models.Profile(user=instance)
        # assign_perm("permission", instance, ReferralsObject)
        profile.save()

