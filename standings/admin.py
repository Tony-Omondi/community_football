from django.contrib import admin
from .models import Standing

@admin.register(Standing)
class StandingAdmin(admin.ModelAdmin):
    list_display = ('team', 'tournament', 'played', 'won', 'drawn', 'lost', 'goals_for', 'goals_against', 'goal_difference', 'points')
    list_filter = ('tournament',)
    search_fields = ('team__name', 'tournament__name')
