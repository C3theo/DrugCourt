from django.db import models
from model_utils import Choices

class Provider(models.Model):
    CHOICES = Choices('Drug Court', 'Other')
    name = models.CharField(max_length=60)
    provider_type = models.CharField(choices=CHOICES, max_length=20)
    clients = models.ManyToManyField('intake.Client', through='Referral')

    def __str__(self):
        return f'{self.name}'