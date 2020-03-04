from django.forms import ModelForm
from .models import TxAttendance, Objectives, ProbGoals

from django.forms.widgets import DateInput, TimeInput, Textarea


class ProbGoalsForm(ModelForm):
    """

    """

    class Meta:
        model = ProbGoals
        fields = ['client',
                  'objective',
                  'prob_description',
                  'goal_description',
                  'prob_goal_num',
                  'prob_goal_target',
                  'prob_goal_status',
                  'status_date', ]


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
                   'time_out': TimeInput(attrs={'type': 'time'})}


class ObjectivesForm(ModelForm):
    met_date = DateInput(attrs={'type': 'date'})
    obj_target = DateInput(attrs={'type': 'date'})

    class Meta:
        model = Objectives
        fields = ['client', 'description',
                  'obj_num', 'obj_target',
                  'closed', 'met', 'met_date',
                  'tx_rating', 'client_rating', ]

        widgets = {'met_date': DateInput(attrs={'type': 'date'}),
                   'obj_target': DateInput(attrs={'type': 'date'}),
                   'description': Textarea(attrs={'rows': 3, 'cols': 40}),

                   }
