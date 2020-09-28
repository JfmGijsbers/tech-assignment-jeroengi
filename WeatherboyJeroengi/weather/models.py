from django.db import models
from django.utils import timezone

# Create your models here.
class Page(models.Model):
    temperature = models.FloatField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.temperature)
