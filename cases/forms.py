from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Field
from crispy_forms import bootstrap

from .models import Clients, Referrals


class ReferralsClientForm(ModelForm):

    class Meta:
        model = Referrals
        fields = ('clientid', 'firstname', 'middlename', 'lastname',
                  'ssn', 'sex', 'race', 'dob', 'referredby', 'referreddate', 'pretrialname', 'pretrialreceived', 'pretrialcompleted',
                  'pretrialdecision', 'defensename', 'defensereceived', 'defensecompleted', 'defensedecision',
                  'daname', 'dareceived', 'dacompleted', 'dadecision', 'assessname', 'assessreceived', 'assesscompleted',
                  'teamreceived', 'teamcompleted', 'teamdecision')
        labels = {
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
            'dareceived': 'Received',
            'dacompleted': 'Date Completed',
            'dadecision': 'Decision',
            'assessname': 'Name',
            'assessreceived': 'Date Recieved',
            'teamreceived': 'Received',
            'teamcompleted': 'Completed',
            'teamdecision': 'Decision'
        }

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
        self.helper.layout = Layout(
            #   'referredby',
            #   'referreddate',
            bootstrap.TabHolder(
                bootstrap.Tab('Client Info',
                              'clientid',
                              'firstname',
                              'middlename',
                              'lastname',
                              'ssn',
                              'sex',
                              'race',
                              'dob',
                              Submit('save', 'Save Changes')),
                bootstrap.Tab('Pretrial',
                              'pretrialname',
                              'pretrialreceived',
                              'pretrialdecision',
                              Submit('save', 'Save Changes')),
                bootstrap.Tab('Defense',
                              'defensename',
                              'defensereceived',
                              'defensecompleted', 'defensedecision',
                              Submit('save', 'Save Changes')),
                bootstrap.Tab('DA',
                              'daname', 'dareceived', 'dacompleted', 'dadecision',
                              Submit('save', 'Save Changes')),
                bootstrap.Tab('Team',
                              'teamreceived', 'teamcompleted', 'teamdecision',
                              Submit('save', 'Save Changes')),
                bootstrap.Tab('Assessment', 'assessname', 'assessreceived', 'assesscompleted',
                              Submit('save', 'Save Changes')),

            )
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
