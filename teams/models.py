# teams/models.py
from django.db import models

class Team(models.Model):   # 👈 Make sure the class name is Team (Capital T)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
