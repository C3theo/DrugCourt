from django.db import models

class CriminalBackground(models.Model):
    """
        Client Arrest History
    """
    client = models.ForeignKey('intake.Client', on_delete=models.CASCADE)
    arrests = models.IntegerField(db_column='Arrests', blank=True, null=True)
    felonies = models.IntegerField(db_column='Felonies', blank=True, null=True)
    misdemeanors = models.IntegerField(
        db_column='Misdemeanors', blank=True, null=True)
    first_arrest_year = models.IntegerField(
        db_column='FirstArrestYear', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('intake:criminal', kwargs={'pk': self.id})

    def __str__(self):
        return f'CriminalBackGround - Client: {self.client.id}'