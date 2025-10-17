from django.db import models
from django.conf import settings
from teams.models import Team

class Player(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='player_profile_info'   # changed to avoid clash
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='player_members'        # changed to avoid clash
    )
    position = models.CharField(max_length=100)
    number = models.PositiveIntegerField()
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.team.name if self.team else 'No Team'}"
