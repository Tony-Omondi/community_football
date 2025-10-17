from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('official', 'League Official'),
        ('coach', 'Coach'),
        ('player', 'Player'),
        ('fan', 'Fan'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='fan')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


class Player(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='player_profile'
    )
    team = models.ForeignKey(
        'teams.Team',
        on_delete=models.CASCADE,
        related_name='players',
        null=True,
        blank=True
    )
    position = models.CharField(max_length=50, blank=True)
    jersey_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.team.name if self.team else 'No Team'}"


class Coach(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='coach_profile'
    )
    # ✅ Renamed related_name to avoid clash with Team.coach field
    team = models.OneToOneField(
        'teams.Team',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_coach'
    )
    experience_years = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Coach {self.user.get_full_name()} ({self.team.name if self.team else 'No Team'})"


class LeagueOfficial(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='official_profile'
    )
    position = models.CharField(max_length=100, blank=True)
    overseeing_tournaments = models.ManyToManyField(
        'tournaments.Tournament',
        blank=True,
        related_name='officials'
    )

    def __str__(self):
        return f"Official {self.user.get_full_name()} ({self.position})"


# 🔔 Automatically create related profiles when a User is created
@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'coach':
            Coach.objects.create(user=instance)
        elif instance.role == 'official':
            LeagueOfficial.objects.create(user=instance)
        elif instance.role == 'player':
            Player.objects.create(user=instance)
