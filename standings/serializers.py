from rest_framework import serializers
from .models import Standing

class StandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standing
        fields = [
            'id', 'tournament', 'team', 'played', 'won', 
            'drawn', 'lost', 'goals_for', 'goals_against', 
            'goal_difference', 'points'
        ]
