from django.db import models
from django.conf import settings

class Tournament(models.Model):
    TOURNAMENT_TYPES = (
        ('league', 'League'),
        ('cup', 'Cup'),
        ('friendly', 'Friendly'),
    )

    name = models.CharField(max_length=255)
    tournament_type = models.CharField(max_length=50, choices=TOURNAMENT_TYPES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tournaments_created'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_tournament_type_display()})"
