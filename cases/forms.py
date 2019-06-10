from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Button, Submit, Div, Field, Row, HTML
from crispy_forms import bootstrap
from django_fsm import TransitionNotAllowed

from .models import Clients, Referrals


import pdb


class ReferralsClientForm(ModelForm):

    class Meta:

        model = Referrals
        # refid should never be editable
        # status should be editable based off permission - used to check progress (buttons for now)
       
        fields = ['firstname', 'middlename', 'lastname',
                  'ssn', 'sex', 'race', 'dob', 'referredby', 'referreddate', 
                  'pretrialname', 'pretrialreceived', 'pretrialcompleted', 'pretrialdecision', 
                  'defensename', 'defensereceived', 'defensecompleted', 'defensedecision',
                  'daname', 'dareceived', 'dacompleted', 'dadecision',
                  'teamreceived', 'teamcompleted', 'teamdecision',
                  'assessname', 'assessreceived', 'assesscompleted',
                  ]
    

        labels = {
          
            # Client Info
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
            'defensedecision': 'Defense Decision',

            'daname': 'Name',
            'dareceived': 'Date Received',
            'dacompleted': 'Date Completed',
            'dadecision': 'DA Decision',

            'assessname': 'Name',
            'assessreceived': 'Date Recieved',
            'assesscompleted': 'Date Completed',

            'teamreceived': 'Date Received',
            'teamcompleted': 'Date Completed',
            'teamdecision': 'Team Decision'
        }

# sender = forms.EmailField(help_text='A valid email address, please.')
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

# TODO" make formset factory
# why??

class ReferralsTabs(ReferralsClientForm):

    def __init__(self, *args, **kwargs):
        super(ReferralsTabs, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.field_class = 'form-control-md'
        self.helper.layout = Layout(

            Div(
                HTML(
                    "<div class=\"border\">Status: {{ object.status }}</div>"),
                HTML(
                    "<div class=\"border\">ClientID: {{ object.clientid }}</div>"),
                HTML(
                    "<div class=\"border\">RefID: {{ object.refid }}</div>"),
                HTML(
                    "<div class=\"border\">Date Created: {{ object.created }}</div>"),
                # All Decicisions displayed on main page
                HTML("<div class=\"border pb-5\">Decisions:</div>"),

                Field('referreddate', css_class='col-3'),
                Field('referredby', css_class='col-3'),
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

            ),
            Submit(
                'save', 'Save Changes', css_class='btn btn-success mt-3'),
            Button('cancel', 'Cancel', css_class='btn btn-secondary mt-3'),

        )

    

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
