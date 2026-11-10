import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from plants.models import Plant


# Create your models here
class CareLog(models.Model):
    class CareTypeChoices(models.TextChoices):
        FERTILIZING = 'Fertilizing', 'Fertilizing'
        WATERING = 'Watering', 'Watering'
        PRUNING = 'Pruning', 'Pruning'
        REPOTTING = 'Repotting', 'Repotting'

    care_type = models.CharField(
        max_length=20,
        choices=CareTypeChoices.choices,
    )

    date_performed = models.DateField(
        auto_now=False,
        validators=[MaxValueValidator(datetime.date.today())])

    notes = models.TextField(
        max_length=500,
        blank=True
    )

    performed_minutes = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1),
                    MaxValueValidator(60)]
    )

    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.care_type} - {self.plant.scientific_name}"

    class Meta:
        ordering = ['-date_performed']

