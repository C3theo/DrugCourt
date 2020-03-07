from rest_framework import serializers

from .models import Objectives, ProbGoals


class ProbGoalsSerializer(serializers.HyperlinkedModelSerializer):
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


class ObjectivesSerializer(serializers.HyperlinkedModelSerializer):
    goals = ProbGoalsSerializer(many=True)
    class Meta:
        model = Objectives
        fields = ['client', 'description',
                  'obj_num', 'obj_target',
                  'closed', 'met', 'met_date',
                  'tx_rating', 'client_rating', 'goals']

                #   https://www.django-rest-framework.org/api-guide/relations/#nested-relationships