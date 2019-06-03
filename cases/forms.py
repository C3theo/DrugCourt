from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Field, Row, HTML
from crispy_forms import bootstrap

from .models import Clients, Referrals


class ReferralsClientForm(ModelForm):
  

    class Meta:

        model = Referrals
        # how to change field widget
        fields = ('clientid', 'status', 'firstname', 'middlename', 'lastname',
                  'ssn', 'sex', 'race', 'dob', 'referredby', 'referreddate', 'pretrialname', 'pretrialreceived', 'pretrialcompleted',
                  'pretrialdecision', 'defensename', 'defensereceived', 'defensecompleted', 'defensedecision',
                  'daname', 'dareceived', 'dacompleted', 'dadecision', 'assessname', 'assessreceived', 'assesscompleted',
                  'teamreceived', 'teamcompleted', 'teamdecision', 'created')
        
        widget = {
            'status': forms.Textarea,
        }
        
        labels = {
            'created': 'Created Date',
            'status': 'Referral Status',

            # Client Info
            'clientid': 'ClientID',
            'firstname': 'First Name',
            'middlename': 'Middle Name',
            'lastname': 'Last Name',
            'ssn': 'Social Security Number',
            'dob': 'Date of Birth',

            # Reviews
            'referredby': 'Referred By',
            'referreddate': 'Referred Date',
            'pretrialname': 'Name',
            'pretrialreceived': 'Date Received',
            'pretrialcompleted': 'Date Completed',
            'pretrialdecision': 'Decision',
            'defensename': 'Name',
            'defensereceived': 'Date Received',
            'defensecompleted': 'Date Completed',
            'defensedecision': 'Decision',
            'daname': 'Name',
            'dareceived': 'Date Received',
            'dacompleted': 'Date Completed',
            'dadecision': 'Decision',
            'assessname': 'Name',
            'assessreceived': 'Date Recieved',
            'assesscompleted': 'Date Completed',
            'teamreceived': 'Date Received',
            'teamcompleted': 'Date Completed',
            'teamdecision': 'Decision'
        }

# sender = forms.EmailField(help_text='A valid email address, please.')

# Field.disabled¶
    # refid
    # autoincrement ClientID and refID
    # clientid
    # casenumsank
    # chargesnk
    # spn
    # stat
    # lastname
    # firstname
    # middlename
    # ssn
    # track
    # rejectreason
    # dob
    # race
    # sex
    # status
    # division
    # location
    # cell
    # referredby
    # referreddate
    # pretrialname
    # pretrialreceived
    # pretrialcompleted
    # pretrialdecision
    # defensename
    # defensereceived
    # defensecompleted
    # defensedecision
    # daname
    # dareceived
    # dacompleted
    # dadecision
    # assessname
    # assessreceived
    # teamreceived
    # teamcompleted
    # teamdecision
    # arrests
    # felonies
    # misdemeanors
    # firstarrestyear
    # created
    # userid
    # accepteddate
    # county
    # type
    # termreason


class ReferralsTabs(ReferralsClientForm):
    # this needs to be a formset factory

    def __init__(self, *args, **kwargs):
        super(ReferralsTabs, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.field_class = 'form-control-md'
# add created date
        self.helper.layout = Layout(
            
            Div(
                Field('clientid', readonly=True, css_class='col-3'),
                # Only display Field
                HTML("<div class=\"border\">Status: {{ object.status }}</div>"),
                # Field('status', css_class='col-4', readonly=True),
                Field('created', css_class='col-3', readonly=True),
                Field('referreddate', css_class='col-3'),
                Field('referredby', css_class='col-3'),
                # All Decicision displayed on main page
                HTML("<div class=\"border pb-5\">Decisions:</div>"),

                css_class='container border border-dark mb-4'
            ),
            bootstrap.TabHolder(
                # Buttons with dropdowns
                bootstrap.Tab('Client Info',
                              Div(
                                  Row(
                                      Field('firstname', wrapper_class='col'),
                                      Field('middlename',
                                            wrapper_class='col-3', ),
                                      Field('lastname', wrapper_class='col')
                                  ),
                                  Field('ssn', css_class='col-3'),
                                  Field('sex', css_class='col-1'),
                                  Field('race', css_class='col-3'),
                                  Field('dob', css_class='col-4'),
                                  css_class='container border border-dark')
                              ),
                bootstrap.Tab('Pretrial',
                              Div(
                                  Field('pretrialname', css_class='col-6'),
                                  Row(
                                      Field('pretrialreceived',
                                            wrapper_class='col'),
                                      Field('pretrialcompleted',
                                            wrapper_class='col')
                                  ),
                                  Field('pretrialdecision', css_class='col-6'),

                                  css_class='container border border-dark')),
                bootstrap.Tab('Defense',
                              Div(
                                  Field('defensename', css_class='col-6'),
                                  Row(Field('defensereceived', wrapper_class='col'),
                                      Field('defensecompleted', wrapper_class='col')),
                                  Field('defensedecision', css_class='col-6'),
                                  css_class='container border border-dark'

                              )),
                bootstrap.Tab('DA',
                              Div(
                                  Field('daname', css_class='col-6'),
                                  Row(Field('dareceived', wrapper_class='col'),
                                      Field('dacompleted', wrapper_class='col')
                                      ),
                                  Field('dadecision', css_class='col-6'),
                                  css_class='container border border-dark'
                              )),
                bootstrap.Tab('Team',
                              Div(
                                  Row(Field('teamreceived', wrapper_class='col'),
                                      Field('teamcompleted', wrapper_class='col')),
                                  Field('teamdecision', css_class='col-6'),
                                  css_class='container border border-dark'
                              )),
                bootstrap.Tab('Assessment',
                Div(
                              Field('assessname', css_class='col-6'),
                              Row(Field('assessreceived', wrapper_class='col'),
                                  Field('assesscompleted', wrapper_class='col')),
                                css_class='container border border-dark'
                              )),

            )
            ,(Submit('save', 'Save Changes'))
        )


# 'defensename', 'defensereceived', 'defensecompleted', 'defensedecision',
# 'daname', 'dareceived', 'dacompleted', 'dadecision', 'assessname', 'assessreceived', 'assesscompleted',
# 'teamreceived', 'teamcompleted', 'teamdecision'


class ClientsForm(ModelForm):

    class Meta:
        model = Clients
        fields = ('clientid', 'cellphone', 'email')
        labels = {
            'clientid': 'Client ID',
            'cellphone': 'Phone Number'
        }


class ClientsTabForm(ClientsForm):

    def __init__(self, *args, **kwargs):
        super(ClientsTabForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            bootstrap.TabHolder(
                bootstrap.Tab('Contact Info',
                              'clientid',
                              'cellphone',
                              'email',
                              Submit('save', 'Save Changes')),
            )
        )
