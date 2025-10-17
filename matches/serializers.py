from rest_framework import serializers
from .models import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = [
            'id', 'tournament', 'home_team', 'away_team', 
            'match_date', 'location', 'home_score', 
            'away_score', 'status', 'referee', 'created_at'
        ]
