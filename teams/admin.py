from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'tournament', 'coach', 'created_at')
    search_fields = ('name', 'tournament__name', 'coach__username')
    list_filter = ('tournament',)
