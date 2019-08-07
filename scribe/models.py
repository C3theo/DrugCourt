"""
    Scribe App Models
"""

from django.db import models
from model_utils import Choices

class Note(models.Model):
    """
        Model to represent Client Notes.

        Fields:
            text
            created_date
            note_type
            client
    """

    CHOICES = Choices('Court', 'Treatment', 'General')
    # TODO: add user as model
    # author = models.ForeignKey(
    #     Profile, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(help_text='Enter notes here.')
    created_date = models.DateTimeField(auto_now_add=True)
    note_type = models.CharField(
        choices=CHOICES, max_length=25, null=True, blank=True)

    # TODO: Make many to many for group notes
    client = models.ForeignKey(
        'intake.Client', related_name='client_notes', on_delete=models.CASCADE)

    class Meta:
        managed = True
        app_label = 'intake'
        verbose_name_plural = 'notes'

    def __str__(self):
        return f'Note: {self.client.client_id}'