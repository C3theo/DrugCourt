from core.helpers.factories import *
from treatment.models import Objectives, ProbGoals, ProbGoalStatusOptions


@factory.django.mute_signals(post_save)
class ObjectivesFactory(DjangoModelFactory):
    class Meta:
        model = Objectives
    client = factory.SubFactory('intake.models.factories.ClientFactory')
    description = factory.Faker('sentences', nb=1, ext_word_list=None)
    obj_num = factory.Faker('random_element', elements=[
        x for x in range(1, 10)])
    obj_target = factory.Faker(
        'date_this_decade', before_today=False, after_today=True)
    closed = factory.Faker('boolean', chance_of_getting_true=50)
    met = factory.Faker('boolean', chance_of_getting_true=50)
    met_date = factory.Faker(
        'date_this_decade', before_today=False, after_today=True)
    tx_rating = factory.Faker('random_element', elements=[
        x for x in range(1, 10)])
    client_rating = factory.Faker('random_element', elements=[
        x for x in range(1, 10)])

    # probgoals = factory.RelatedFactory(
    #     'treatment.models.factories.ProbGoals', 'client')

    @factory.helpers.post_generation
    def probgoals(self, create, extracted, **kwargs):
        """
            Creates a random number of ProbGoal Instances
        """
        if not create:
            return

        if extracted:
            assert isinstance(extracted, int)
            ProbGoalsFactory.create_batch(
                size=extracted, client=self.client, objective=self, **kwargs)
        else:
            import random
            number_of_units = random.randint(1, 5)
            for n in range(number_of_units):
                ProbGoalsFactory(client=self.client, objective=self)


@factory.django.mute_signals(post_save)
class ProbGoalsFactory(DjangoModelFactory):
    """
    """

    class Meta:
        model = ProbGoals
    client = factory.SubFactory('intake.models.factories.ClientFactory')
    objective = factory.SubFactory(
        'treatment.models.factories.ObjectivesFactory')
    prob_description = factory.Faker('sentences', nb=1, ext_word_list=None)
    goal_description = factory.Faker('sentences', nb=1, ext_word_list=None)
    prob_goal_num = factory.Faker('random_element', elements=[
        x for x in range(1, 10)])
    prob_goal_target = factory.Faker(
        'date_this_decade', before_today=False, after_today=True)
    prob_goal_status = factory.Faker('random_element', elements=[
        x[0] for x in ProbGoalStatusOptions.CHOICES])
    status_date = prob_goal_target = factory.Faker(
        'date_this_decade', before_today=False, after_today=True)
