from rest_framework import serializers

from .models import Objectives, ProbGoals


class ProbGoalsSerializer(serializers.HyperlinkedModelSerializer):
    
    objective = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProbGoals
        fields = ['client',
                  'objective',
                  'prob_description',
                  'goal_description',
                  'prob_goal_num',
                  'prob_goal_target',
                  'prob_goal_status',
                  'status_date', 'id']


class ObjectivesSerializer(serializers.HyperlinkedModelSerializer):
    goals = ProbGoalsSerializer(many=True)
    client = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Objectives
        fields = ['pk', 'client', 'description',
                  'obj_num', 'obj_target',
                  'closed', 'met', 'met_date',
                  'tx_rating', 'client_rating', 'goals']

        #   https://www.django-rest-framework.org/api-guide/relations/#nested-relationships

    def create(self, validated_data):
        goals = validated_data.pop('goals')
        objective = Objectives.objects.create(**validated_data)
        for goal in goals:
            ProbGoals.objects.create(objective=objective, **goal)
        return objective

