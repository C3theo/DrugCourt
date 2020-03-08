import logging
import string
from datetime import date
from random import randrange

import factory
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.utils import timezone
from factory import DjangoModelFactory

# from intake.models import ClientFactory


# def create_pending_clients(factory.):


def populate_fake_db(factory=None, size=25):
    """
        Helper function to create fake Models instances.
    """

    factory.create_batch(size)


## This is dumb
def delete_factory_inventory(factory=None):
    try:
        model = factory._meta.model
    except Exception:
        model = factory
    inventory = model.objects.all()
    for each in inventory:
        each.delete()

    return f'{len(inventory)} objects deleted'