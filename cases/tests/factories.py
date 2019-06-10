from factory import DjangoModelFactory
import logging
import factory
from cases.models import Referrals, Clients
from datetime import date

from random import randrange

def delete_all_Referrals():
    for obj in Referrals.objects.all():
        obj.delete()

def create_fake_referrals(size=None):
    ReferralsFactory.create_batch(size=size)


class ReferralsFactory(DjangoModelFactory):
    class Meta:
        model = Referrals
        # strategy = factory.BUILD_STRATEGY
        django_get_or_create = ('refid', 'clientid', 'firstname', 'middlename', 'lastname', 'created', 'ssn', 'status', 'track', 'sex',
                                'dadecision', 'teamdecision', 'defensedecision', 'pretrialdecision')

    refid = factory.Sequence(lambda n: f'{n}')
    clientid = factory.Sequence(lambda n: f'{int(2019000) + n}')
    # clientid = factory.RelatedFactory(ClientsFactory, 'clientid')

    firstname = factory.Faker('first_name')
    middlename = factory.Faker('first_name')
    lastname = factory.Faker('last_name')
    created = factory.Faker('date_time_this_month')
    
    ssn = factory.Faker('ssn')
    status = factory.Faker('random_element', elements=[
                           x[0] for x in Referrals.STATUS_CHOICES])

    # casenums = factory.Faker()
    # charges = factory.Faker('random_element', elements=[])
    # spn = factory.Sequence(lambda n:  f'21231')
    track = randrange(1, 4)
    # rejectreason = factory.Faker('random_element', elements=[])
    dob = factory.Faker('date_of_birth')
    # race = factory.Iterator('random_element', elements=[Referrals.objects.distinct('race')]) this will only work if models are prepopulated
    sex = factory.Faker('random_element', elements=['M', 'F'])
    # division = factory.Faker('random_element', elements=[])
    # location = factory.Faker('random_element', elements=[])

    # Use distinct values
    # cell = factory.Iterator(Referrals.objects.distinct('cell'))
    referredby = factory.Faker('name')
    referreddate = factory.Faker('date_this_year')

    pretrialname = factory.Faker('name')
    pretrialreceived = factory.Faker('past_date', start_date='-30d')
    pretrialcompleted = date.today()
    pretrialdecision = factory.Faker('random_element', elements=[
                                     x[0] for x in Referrals.STATUS_DECISION])

    defensename = factory.Faker('name')
    defensereceived = factory.Faker('past_date', start_date='-30d')
    defensecompleted = date.today()
    defensedecision = factory.Faker('random_element', elements=[
                                    x[0] for x in Referrals.STATUS_DECISION])

    daname = factory.Faker('name')
    dareceived = factory.Faker('past_date', start_date='-30d')
    dacompleted = date.today()
    dadecision = factory.Faker('random_element', elements=[
                               x[0] for x in Referrals.STATUS_DECISION])

    assessname = factory.Faker('name')
    assessreceived = factory.Faker('past_date', start_date='-30d')
    assesscompleted = date.today()

    teamreceived = factory.Faker('past_date', start_date='-30d')
    teamcompleted = date.today()
    teamdecision = factory.Faker('random_element', elements=[
                                 x[0] for x in Referrals.STATUS_DECISION])

    # arrests = factory.Faker('random_element', elements=range(0, 50))
    arrests = randrange(1, 20)
    # felonies = factory.Faker('random_element', elements=[range(0, 50)])
    arrests = randrange(1, 20)
    # misdemeanors = factory.Faker('random_element', elements=[range(0, 50)])
    misdemeanors = randrange(1, 20)
    firstarrestyear = factory.Faker('year')

    userid = factory.Sequence(lambda n: f'UserID:{n}')
    # factory.SubField
    # accepteddate = factory.Faker('date_time')
    # dependent on status
    county = factory.Sequence(lambda n: f'County {n}')
    # type = ???
    # termreason = factory.Faker('random_element', elements=[])

    @classmethod
    def _setup_next_sequence(cls):
        try:
            return Referrals.objects.latest('refid').refid + 1
        except Referrals.DoesNotExist:
            # singluar Referral?? - from factoryboy docs
            return 1


class ClientsFactory(DjangoModelFactory):
    class Meta:
        model = Clients
        django_get_or_create = ('id',
                                'clientid',
                                # 'startdate',
                                # 'dischargedate',
                                # 'cellphone',
                                # 'email',
                                # 'message',
                                # 'messagesource',
                                # 'yearlyincome',
                                # 'incomesource',
                                # 'educationyrs',
                                # 'educationlevel',
                                # 'highschoolgrad',
                                # 'ged',
                                # 'militaryservice',
                                # 'vaeligible',
                                # 'maritalstatus',
                                # 'pregnant',
                                # 'children',
                                # 'childnarrative',
                                # 'diagnosis',
                                # 'suicide',
                                # 'violence',
                                # 'health',
                                # 'ghmedications',
                                # 'prenatal',
                                # 'tbstatus',
                                # 'physicalabuse',
                                # 'sexualabuse',
                                # 'insurance',
                                # 'primarydrug',
                                # 'substanceuse',
                                # 'sobriety',
                                # 'needleuse',
                                # 'addictionseverityindex',
                                # 'familyoforiginyn',
                                # 'familyoforiginuse',
                                # 'spouseuseyn',
                                # 'spouseuse',
                                # 'testtype',
                                # 'testresult',
                                # 'employedatgraduation',
                                # 'outcomecomments',
                                # 'cmuserid',
                                # 'couserid',
                                # 'phase',
                                # 'stopbilling',
                                # 'userid',
                                # 'created',
                                # 'ssma_timestamp',
                                # 'lastpositive',
                                # 'lep',
                                # 'employedatstart',
                                # 'employedatgrad',
                                # 'asam_loc',
                                )

    id = factory.Sequence(lambda n: f'{n}')
    
    # clientid = factory.RelatedFactory(ReferralsFactory, 'clientid')
    # Create client when referral created
    # clientid = factory.SubFactory(ReferralsFactory, 'clientid')
    # Error: factory.errors.FactoryError: django_get_or_create - Unable to find initialization value for 'clientid' in factory ReferralsFactory

    startdate = factory.Faker('date_past', startdate='-30d')
    dischargedate = factory.Faker('date_past', startdate='-10d')
    cellphone = factory.Faker('phone')
    email = factory.Faker('email')
    # message = factory
    # messagesource = factory
    # yearlyincome = factory
    # incomesource = factory
    # educationyrs = factory
    # educationlevel = factory
    # highschoolgrad = factory
    # ged = factory
    # militaryservice = factory
    # vaeligible = factory
    # maritalstatus = factory
    # pregnant = factory
    # children = factory
    # childnarrative = factory
    # diagnosis = factory
    # suicide = factory
    # violence = factory
    # health = factory
    # ghmedications = factory
    # prenatal = factory
    # tbstatus = factory
    # physicalabuse = factory
    # sexualabuse = factory
    # insurance = factory
    # primarydrug = factory
    # substanceuse = factory
    # sobriety = factory
    # needleuse = factory
    # addictionseverityindex = factory
    # familyoforiginyn = factory
    # familyoforiginuse = factory
    # spouseuseyn = factory
    # spouseuse = factory
    # testtype = factory
    # testresult = factory
    # employedatgraduation = factory
    # outcomecomments = factory
    # cmuserid = factory
    # couserid = factory
    # phase = factory
    # stopbilling = factory
    # userid = factory
    # created = factory.Factory()
    # ssma_timestamp = factory
    # lastpositive = factory
    # lep = factory
    # employedatstart = factory
    # employedatgrad = factory
    # asam_loc = factory

    @classmethod
    def _setup_next_sequence(cls):
        try:
            return Clients.objects.latest('id').id + 1
        except Clients.DoesNotExist:
            return 1




with factory.debug():
    obj = ReferralsFactory()


logger = logging.getLogger('factory')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
