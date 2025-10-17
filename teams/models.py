from django.db import models
from django.conf import settings
from tournaments.models import Tournament

class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)
    coach = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='coached_teams'
    )
    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.SET_NULL,   # ✅ Changed from CASCADE to SET_NULL
        null=True,
        blank=True,                  # ✅ Makes it optional
        related_name='teams'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_teams'
    )

    def __str__(self):
        return self.name
