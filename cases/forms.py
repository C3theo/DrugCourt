from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Field
from crispy_forms import bootstrap


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
        Pretrial, Defense, DA, Team
    """
    review_type = forms.ChoiceField(label='Review Type', choices=[(1, 'Pretrial'),
                                                                  (2, 'Defense'),
                                                                  (3, 'DA'),
                                                                  (4, 'Team'),
                                                                  (5, 'Assessment')])
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
    first_arrest_year = forms.DateField(
        label='First Arrest Year', input_formats=['%m/%d/%y'])
    enroll_date = forms.DateField(
        label='Enrollment Date', input_formats=['%m/%d/%y'])
    status = forms.ChoiceField(choices=[('1', 'Status_1'),
                                        ('2', 'Status_2'),
                                        ('3', 'Status_3')])
    reject_reason = forms.ChoiceField(label='Rejection Reason', choices=[('1', 'Reason_1'),
                                                                         ('2', 'Reason_2'),
                                                                         ('3', 'Reason_3')])

    court_notes = forms.CharField(label='Court Notes', widget=forms.Textarea)


class ClientTabForm(ClientForm, ReviewForm, ReferralForm):
    # TODO: Create Tabbed Headers

    def __init__(self, *args, **kwargs):
        super(ClientTabForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            bootstrap.TabHolder(
                bootstrap.Tab('Client Info',
                              'first_name',
                              'middle_name',
                              'last_name',
                              'email',
                              'ssn',
                              'ethnicity',
                              'gender',
                              'date_of_birth',
                              Submit('save', 'Save Changes')),
                bootstrap.Tab('Case Info',
                              'spn',
                              'state_id',
                              'division',
                              'location',
                              'case_numbers',
                              'referred_by',
                              'track',
                              Submit('save', 'Save Changes')),
                bootstrap.Tab('Reviews',
                              'review_type',
                              'review_by',
                              'date_received',
                              'decision',
                              Submit('save', 'Save Changes')),
                bootstrap.Tab('Criminal History',
                              'arrests',
                              'felonies',
                              'misdemeanors',
                              'first_arrest_year',
                              Submit('save', 'Save Changes')),
                bootstrap.Tab('Referrals',
                              'els',
                              'cell',
                              'enroll_date',
                              'status',
                              'reject_reason',
                              'court_notes',
                              Submit('save', 'Save Changes'))
            )
        )
        # TODO: remove review_by field if type == team


class EmployerForm(forms.Form):
    employer_name = forms.CharField(label='Employer')
    employer_address = forms.CharField(label='Address')
    city = forms.CharField()
    # TODO: add all state abbreviations
    state = forms.ChoiceField(choices=[('1', 'GA'), ])
    zip_code = forms.CharField(label='Zip')
    contact = forms.CharField()
    phone = forms.CharField()
    hire_date = forms.DateField(
        label='Hire Date', input_formats=['%m/%d/%y'])
    term_date = forms.DateField(
        label='Term Date', input_formats=['%m/%d/%y'])
    hourly_income = forms.IntegerField(label='Hourly Income')
    hours_week = forms.IntegerField(label='Weekly Hours')
    schedule = forms.DurationField()
    pay_period = forms.DurationField()


class SanctionForm(forms.Form):
    sanction_date = forms.DateField(
        label='Sanction Date', input_formats=['%m/%d/%y'])
    sanction_level = forms.ChoiceField(
        label='Sanction Level', choices=[('1', 'Sanction 1')])
    sanction_notes = forms.CharField(label='Sanction Notes')
    from_date = forms.DateField(
        label='Jail Start Date', input_formats=['%m/%d/%y'])
    to_date = forms.DateField(label='Jail End Date',
                              input_formats=['%m/%d/%y'])
    jail_days = forms.DurationField(label='Jail Days')
    cs_provider = forms.CharField(label='CS Provider')
    # total_hours =


class CourtPhaseForm(forms.Form):
    user_id = forms.CharField(label='User ID')
    client_id = forms.CharField(label='User ID')
    phase = forms.ChoiceField(choices=[('1', 'Phase 1')])
    phase_start = forms.DateField(
        label='Phase Start', input_formats=['%m/%d/%y'])
    phase_end = forms.DateField(
        label='Phase End', input_formats=['%m/%d/%y'])
    complete = forms.BooleanField(label='Complete')
    freeze_start = forms.DateField(
        label='Freeze Start', input_formats=['%m/%d/%y'])
    freeze_end = forms.DateField(
        label='Freeze End', input_formats=['%m/%d/%y'])
    discharge = forms.CharField()


class CourtDateForm(forms.Form):
    court_date = forms.DateField(
        label='Phase Start', input_formats=['%m/%d/%y'])
    court_type = forms.ChoiceField(choices=[('1', 'Type 1'), ])
    event = forms.ChoiceField(choices=[('1', 'Event 1'), ])
    attendance = forms.ChoiceField(choices=[('1', 'Attendance 1'), ])
    comments = forms.CharField()


class CourtFeeForm(forms.Form):
    transaction_date = forms.DateField(
        label='Transaction Date', input_formats=['%m/%d/%y'])
    amount = forms.DecimalField(label='Payment Amount')
    billing_info = forms.IntegerField(label='Billing Info')
    user_id = forms.CharField()
    # paid =
    # billed =
    # balance =
    submitted = forms.BooleanField(label='Submitted')
    accepted_by = forms.CharField()
    submit_date = forms.DateField(
        label='Transaction Date', input_formats=['%m/%d/%y'])
    stop_billing = forms.BooleanField(label='Stop Billing')


class CourtFineForm(forms.Form):
    transaction_date = forms.DateField(
        label='Transaction Date', input_formats=['%m/%d/%y'])
    amount = forms.DecimalField(label='Payment Amount')
    billing_info = forms.IntegerField(label='Billing Info')
    user_id = forms.CharField()
    paid = forms.IntegerField()
    billed = forms.IntegerField()
    balance = forms.IntegerField()
    submitted = forms.BooleanField(label='Submitted')
    entered_by = forms.CharField(label='Entered By')
    submit_date = forms.DateField(
        label='Transaction Date', input_formats=['%m/%d/%y'])
    # Note: Enter fine as a negative amount and payment as a positive amount.


class CourtRewardForm(forms.Form):
    court_date = forms.DateField(label='Court Date')
    court_id = forms.ChoiceField(
        label='Court ID', choices=[('1', 'Court ID 1')])
    court_reward = forms.ChoiceField(label='Reward')


class CourtProposalForm(forms.Form):
    client_id = forms.ChoiceField(label='Client ID')
    proposal_date = forms.DateField(label='Proposal Date')
    proposal_type = forms.ChoiceField(
        label='Proposal Type', choices=[('1', 'Proposal Type')])
    proposal_status = forms.ChoiceField(
        label='Proposal Status', choices=[('1', 'Proposal Status')])
    pass_start = forms.DateField(
        label='Pass Start', input_formats=['%m/%d/%y'])
    pass_end = forms.DateField(label='Approve End',
                               input_formats=['%m/%d/%y'])
    approve_date = forms.DateField(
        label='Pass End', input_formats=['%m/%d/%y'])
    entered_by = forms.CharField(label='Entered By')
    approver = forms.CharField()
    proposal_description = forms.CharField(label='Proposal Description')
    proposal_comment = forms.CharField(label='Proposal Comment')


class DrugScreenForm(forms.Form):
    collect_date = forms.DateField(
        label='Collect Date', input_formats=['%m/%d/%y'])
    result = forms.CharField()
    positive_result = forms.BooleanField(label='Approved Positive?')
    drugs_found = forms.BooleanField(label='Drugs Found?')
    display_positives = forms.BooleanField(label='Display Positives')
    # client_id
    # user_id


class CommunityServiceForm(forms.Form):
    cs_date = forms.DateField(label='Service Date',
                              input_formats=['%m/%d/%y'])
    cs_assignment = forms.CharField(label='Community Service Assignment')
    cs_hours = forms.IntegerField(label='Service Hours')
    cs_verified_by = forms.CharField(label='Verified By')
    total_hours = forms.DurationField(label='Total Hours Worked')

# class OutreachForm(forms.Form):


class CourtTabForm(CourtPhaseForm):

    def __init__(self, *args, **kwargs):
        super(CourtTabForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            bootstrap.TabHolder(
                bootstrap.Tab('Court Phases',
                              'user_id',
                              'client_id',
                              'phase',
                              'phase_start',
                              'phase_end',
                              'complete',
                              'freeze_start',
                              'freeze_end',
                              'discharge',
                              Submit('save', 'Save Changes'))
            )
        )


class TreatmentForm(forms.Form):
    pass
