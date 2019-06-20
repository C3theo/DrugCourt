from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django_fsm import TransitionNotAllowed

from guardian.shortcuts import assign_perm
from .models import Referral


# TODO: check conditions
# DO this another way - check 2 Scoops
@receiver(post_save, sender=Referral)
def referral_status_handler(sender, instance, **kwargs):
    try:
        instance.approve_referral()
        instance.save()

    except TransitionNotAllowed:
        pass
