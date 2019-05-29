from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class ClientForm(forms.Form):

    first_name = forms.CharField(label='First Name')
    middle_name = forms.CharField(label='Middle Name', required=False)
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email', required=False)
    ssn = forms.IntegerField(label='Social Security Number')
    ethnicity = forms.CharField(label='Ethnicity', required=False)
    gender = forms.ChoiceField(
        label='Gender', choices=(('M', 'Male'), ('F', 'Female')))
    date_of_birth = forms.DateField(
        label='Date of Birth', input_formats=['%m/%d/%y'])

    spn = forms.CharField(label='SPN #')
    state_id = forms.CharField(label='State ID')
    division = forms.CharField(label='Division')
    location = forms.CharField(label='Location')
    case_numbers = forms.CharField(label='Case Numbers')
    referred_by = forms.CharField(label='Referred By')
    track = forms.TypedChoiceField(label='Track', choices=[('One', '1'),
                                                           ('Two', '2'),
                                                           ('Three', '3'),
                                                           ('Four', '4'),
                                                           ('Five', '5')],
                                   coerce=int, empty_value=None)


class ReviewForm(forms.Form):
    """
        Pretrial, Defense, DA
    """
    review_type = forms.ChoiceField(label='Review Type', choices=[('1', 'Pretrial'),
                                                                  ('2', 'Defense'),
                                                                  ('3', 'DA')])
    review_by = forms.CharField(label='Review By')
    date_received = forms.DateField(
        label='Date Received', input_formats=['%m/%d/%y'])
    date_received = forms.DateField(
        label='Date Completed', input_formats=['%m/%d/%y'])
    decision = forms.CharField(label='Decision')


class TeamReviewForm(forms.Form):
    date_received = forms.DateField(
        label='Date Received', input_formats=['%m/%d/%y'])
    date_completed = forms.DateField(
        label='Date Completed', input_formats=['%m/%d/%y'])
    team_decision = forms.CharField(label='Team Decision')


class AssesmentForm(forms.Form):
    assessed_by = forms.CharField()
    date_completed = forms.DateField(input_formats=['%m/%d/%y'])
    assessment = forms.CharField()


class ReferralForm(forms.Form):
    # TODO: inherit from client form
    # new fields
    els = forms.CharField(label='ELS')
    cell = forms.CharField()
    arrests = forms.CharField()
    felonies = forms.CharField()
    misdemeanors = forms.CharField()
    first_arrest_year = forms.DateField(label='First Arrest Year', input_formats=['%m/%d/%y'])
    enroll_date = forms.DateField(label='Enrollment Date', input_formats=['%m/%d/%y'])
    status = forms.ChoiceField(choices=[('1', 'Status_1'),
                                               ('2', 'Status_2'),
                                               ('3', 'Status_3')])
    reject_reason = forms.ChoiceField(label='Rejection Reason', choices=[('1', 'Reason_1'),
                                               ('2', 'Reason_2'),
                                               ('3', 'Reason_3')])
    # TODO: Add larger input field
    court_notes = forms.CharField(label='Court Notes')

class CourtForm(forms.Form):
    # TODO: Create Tabbed Headers
    pass

class EmployerForm(forms.Form):
    pass