from django.db import models

from cases.models import Clientaddress, Clients, Referrals
from viewflow.models import Process


# class ReferralProcess(Referrals, Process):
#     approved = models.BooleanField(default=False)

class HelloWorldProcess(Process):
    text = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)
