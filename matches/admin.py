from django.contrib import admin
from .models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'tournament', 'match_date', 'status', 'referee')
    list_filter = ('status', 'tournament', 'match_date')
    search_fields = ('home_team__name', 'away_team__name', 'tournament__name', 'referee__username')
