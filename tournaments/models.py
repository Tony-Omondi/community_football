# tournaments/models.py
from django.db import models

class Tournament(models.Model):   # 👈 Make sure the class name is Tournament (Capital T)
    name = models.CharField(max_length=100)
    start_date = models.DateField()

    def __str__(self):
        return self.name
