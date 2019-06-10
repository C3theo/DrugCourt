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
        fields = ('refid', 'status', 'firstname', 'middlename', 'lastname',
                  'ssn', 'sex', 'race', 'dob', 'referredby', 'referreddate', 'pretrialname', 'pretrialreceived', 'pretrialcompleted',
                  'pretrialdecision', 'defensename', 'defensereceived', 'defensecompleted', 'defensedecision',
                  'daname', 'dareceived', 'dacompleted', 'dadecision', 'assessname', 'assessreceived', 'assesscompleted',
                  'teamreceived', 'teamcompleted', 'teamdecision', 'created')
        # pdb.set_trace()
        # This isn't working
        # widget = {
        #     'status': forms.Textarea,
        # }

        labels = {
            'created': 'Created Date',
            'status': 'Referral Status',

            # Client Info
            # 'clientid': 'ClientID',
            'refid': 'RefID',
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


class ReferralsTabs(ReferralsClientForm):

    def __init__(self, *args, **kwargs):
        super(ReferralsTabs, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.field_class = 'form-control-md'

        self.helper.layout = Layout(

            Div(
                # Only display Field
                HTML(
                    "<div class=\"border\">Status: {{ object.status }}</div>"),
                HTML(
                    "<div class=\"border\">ClientID: {{ object.clientid }}</div>"),
                HTML(
                    "<div class=\"border\">RefID: {{ object.refid }}</div>"),
                # Field('refid', css_class='col-4'),
                # TODO: need a way to change all assessments
                # Field('status', css_class='col-4'),
                Field('created', css_class='col-3'),
                Field('referreddate', css_class='col-3'),
                Field('referredby', css_class='col-3'),

                # All Decicision displayed on main page
                HTML("<div class=\"border pb-5\">Decisions:</div>"),
                Submit('approve', 'Approve Client', css_class='btn btn-dark'),
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
            # Button('cancel', 'Cancel', css_class='btn btn-secondary mt-3'),

        )

    # https://stackoverflow.com/questions/2432489/django-overwrite-form-clean-method
    # def clean(self, *args, **kwargs):
    #     if 'approve' in self.data:
    #         try:
    #             self.instance.approve_referral()
    #             # self.instance.save() cannot save instance like this
    #         except TransitionNotAllowed:
    #             pass

    #     super().clean(*args, **kwargs)


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
