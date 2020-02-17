from django.forms import ModelForm
from .models import TxSession, Objective

from django.forms.widgets import DateInput, TimeInput


class TxAttendanceForm(ModelForm):
    session_date = DateInput(attrs={'type': 'date'})
    time_in = TimeInput(attrs={'type': 'time'})
    time_out = TimeInput(attrs={'type': 'time'})

    class Meta:
        model = TxSession
        fields = ['client', 'session_date', 'attended', 'absence_reason', 'time_in',
                  'time_out']
        widgets = {'session_date': DateInput(attrs={'type': 'date'}),
                   'time_in': TimeInput(attrs={'type': 'time'}),
                   'time_out': TimeInput(attrs={'type': 'time'})}


class ObjectivesForm(ModelForm):
    met_date = DateInput(attrs={'type': 'date'})
    obj_target = DateInput(attrs={'type': 'date'})

    class Meta:
        model = Objective
        fields = ['client', 'description',
                    'obj_num', 'obj_target',
                    'closed', 'met', 'met_date',
                    'tx_rating', 'client_rating', ]

        widgets = {'met_date': DateInput(attrs={'type': 'date'}),
                'obj_target': DateInput(attrs={'type': 'date'})}
