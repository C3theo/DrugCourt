from django.forms import ModelForm
from .models import TxAttendance

from django.forms.widgets import DateInput, TimeInput


class TxAttendanceForm(ModelForm):
    session_date = DateInput(attrs={'type': 'date'})
    time_in = TimeInput(attrs={'type': 'time'})
    time_out = TimeInput(attrs={'type': 'time'})

    class Meta:
        model = TxAttendance
        fields = ['client', 'session_date', 'attended', 'absence_reason', 'time_in',
                  'time_out']
        widgets = {'session_date': DateInput(attrs={'type': 'date'}),
                   'time_in': TimeInput(attrs={'type': 'time'}),
                   'time_out': TimeInput(attrs={'type': 'time'})
                   }
