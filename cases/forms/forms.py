from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Button, Submit, Div, Field, Row, HTML
from crispy_forms import bootstrap
from django_fsm import TransitionNotAllowed

from ..models import Clients, Referrals

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
            'sex': '<i class="fas fa-venus-mars"></i> Sex',

            # Reviews
            'referredby': 'Referred By',
            'referreddate': 'Referred Date',
            'pretrialname': 'Name',
            'pretrialreceived': '<i class="fas fa-calendar-day"></i> Date Received',
            'pretrialcompleted': '<i class="fas fa-calendar-day"></i> Date Completed',
            'pretrialdecision': '<i class="fas fa-gavel"></i> Pretrial Decision',

            'defensename': 'Name',
            'defensereceived': '<i class="fas fa-calendar-day"></i> Date Received',
            'defensecompleted': '<i class="fas fa-calendar-day"></i> Date Completed',
            'defensedecision': '<i class="fas fa-gavel"></i> Defense Decision',

            'daname': 'Name',
            'dareceived': '<i class="fas fa-calendar-day"></i> Date Received',
            'dacompleted': '<i class="fas fa-calendar-day"></i> Date Completed',
            'dadecision': '<i class="fas fa-gavel"></i> DA Decision',

            'assessname': 'Name',
            'assessreceived': '<i class="fas fa-calendar-day"></i> Date Recieved',
            'assesscompleted': '<i class="fas fa-calendar-day"></i> Date Completed',

            'teamreceived': '<i class="fas fa-calendar-day"></i> Date Received',
            'teamcompleted': '<i class="fas fa-calendar-day"></i> Date Completed',
            'teamdecision': '<i class="fas fa-gavel"></i> Team Decision'
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

class ReferralsTabs(ReferralsClientForm):
    def __init__(self, *args, **kwargs):
        super(ReferralsTabs, self).__init__(*args, **kwargs)
        tab_class = ''
        self.fields['firstname'].required = True
        self.fields['sex'].required = True
        self.fields['lastname'].required = True
        self.fields['referredby'].required = True
        self.fields['referreddate'].required = True

        self.helper = FormHelper()
        self.helper.field_class = 'form-control-md'
        self.helper.add_input(
            Submit('submit', 'Submit', css_class='mt-3', style='width:100px'))
        self.helper.layout = Layout(

            

            Div(
                bootstrap.TabHolder(
                    # TODO: Buttons with dropdowns
                    bootstrap.Tab('Contact Info',
                                  Div(
                                      Row(
                                          Field('firstname',
                                                wrapper_class='col'),
                                          Field('middlename',
                                                wrapper_class='col-3', ),
                                          Field('lastname', wrapper_class='col')
                                      ),
                                      Field('ssn', css_class='col-3'),
                                      Field('sex', css_class='col-3'),
                                      Field('race', css_class='col-3'),
                                      HTML("""
                                 <div id="div_id_dob" class="form-group"> <label for="id_dob" class="col-form-label">
                                 <i class="fas fa-birthday-cake"></i> Date of Birth</label> <div class="form-control-md">
                                <input type="text" name="dob" class="col-4 dateinput form-control" id="id_dob"> </div> </div>
                                  """),
                                  Field('referreddate', wrapper_class='col-4'),
                Field('referredby', wrapper_class='col-4'),
                                      css_class=tab_class)
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
                                      Field('pretrialdecision',
                                            css_class='col-6'),
                                      #       HTML("""
                                      # <div id="div_id_pretrialdecision" class="form-group">
                                      # <label for="id_pretrialdecision" class="col-form-label"><i class="fas fa-gavel"></i> Pretrial Decision
                                      # </label> <div class="form-control-md"> <select name="pretrialdecision" class="col-6 select form-control" id="id_pretrialdecision">
                                      # <option value="">---------</option>
                                      # <option value="Approved">Approved</option>
                                      # <option value="Rejected">Rejected</option>
                                      # </select> </div> </div>
                                      # """),
                                      css_class=tab_class)),
                    bootstrap.Tab('Defense',
                                  Div(
                                      Field('defensename', css_class='col-6'),
                                      Row(Field('defensereceived', wrapper_class='col'),
                                          Field('defensecompleted', wrapper_class='col')),
                                      Field('defensedecision',
                                            css_class='col-6'),
                                      #                                       HTML("""
                                      #                                 <div id="div_id_defensedecision" class="form-group"> <label for="id_defensedecision" class="col-form-label "><i class="fas fa-gavel"></i> Defense Decision
                                      #             </label> <div class="form-control-md"> <select name="defensedecision" class="col-6 select form-control" id="id_defensedecision">
                                      #             <option value="">---------</option> <option value="Approved">Approved</option> <option value="Rejected">Rejected</option>

                                      # </select> </div> </div>
                                      #                                """),
                                      css_class=tab_class

                                  )),
                    bootstrap.Tab('DA',
                                  Div(
                                      Field('daname', css_class='col-6'),
                                      Row(Field('dareceived', wrapper_class='col'),
                                          Field('dacompleted',
                                                wrapper_class='col')
                                          ),
                                        Field('dadecision', css_class='col-6'),
#                                       HTML("""
#                                 <div id="div_id_dadecision" class="form-group"> <label for="id_dadecision" class="col-form-label "><i class="fas fa-gavel"></i> DA Decision</label>
#                                 <div class="form-control-md"> <select name="dadecision" class="col-6 select form-control" id="id_dadecision">
#                                 <option value="">---------</option> <option value="Approved">Approved</option> <option value="Rejected">Rejected</option>

# </select> </div> </div>
#                                 """),

                                      css_class=tab_class
                                  )),
                    bootstrap.Tab('Team',
                                  Div(
                                      Row(Field('teamreceived', wrapper_class='col'),
                                          Field('teamcompleted', wrapper_class='col')),
                                        Field('teamdecision', css_class='col-6'),
#                                       HTML("""
#                                 <div id="div_id_teamdecision" class="form-group"> <label for="id_teamdecision" class="col-form-label "><i class="fas fa-gavel"></i> Team Decision
#             </label> <div class="form-control-md"> <select name="teamdecision" class="col-6 select form-control" id="id_teamdecision">
#             <option value="">---------</option> <option value="Approved">Approved</option> <option value="Rejected">Rejected</option>

# </select> </div> </div>
#                                 """),
                                      css_class=tab_class
                                  )),
                    bootstrap.Tab('Assessment',
                                  Div(
                                      Field('assessname', css_class='col-6'),
                                      Row(Field('assessreceived', wrapper_class='col'),
                                          Field('assesscompleted', wrapper_class='col')),
                                      css_class=tab_class
                                  )),
                ),
                css_class='pt-5'),
            # bootstrap.FormActions(
            #     Submit(
            #         'save', 'Save Changes', css_class='btn btn-success'),
            #     Button('cancel', 'Cancel', css_class='btn btn-secondary'), css_class='mt-5'),
        )


# class ClientsForm(ModelForm):

#     class Meta:
#         model = Clients
#         fields = ('clientid', 'cellphone', 'email')
#         labels = {
#             'clientid': 'Client ID',
#             'cellphone': 'Phone Number'
#         }


# class ClientsTabForm(ClientsForm):

#     def __init__(self, *args, **kwargs):
#         super(ClientsTabForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(

#             bootstrap.TabHolder(
#                 bootstrap.Tab('Contact Info',
#                               'clientid',
#                               'cellphone',
#                               'email',
#                               Submit('save', 'Save Changes')),
#             )
#         )
