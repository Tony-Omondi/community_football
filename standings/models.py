from django.db import models
from teams.models import Team
from tournaments.models import Tournament

class Standing(models.Model):
    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE,
        related_name='standings'
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='standings'
    )
    played = models.PositiveIntegerField(default=0)
    won = models.PositiveIntegerField(default=0)
    drawn = models.PositiveIntegerField(default=0)
    lost = models.PositiveIntegerField(default=0)
    goals_for = models.PositiveIntegerField(default=0)
    goals_against = models.PositiveIntegerField(default=0)
    goal_difference = models.IntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('tournament', 'team')
        ordering = ['-points', '-goal_difference', '-goals_for']

    def __str__(self):
        return f"{self.team.name} - {self.tournament.name}"
