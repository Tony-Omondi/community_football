from django.contrib import admin
from .models import Tournament

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'tournament_type', 'start_date', 'end_date', 'created_by')
    search_fields = ('name', 'tournament_type')
