from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models

# Create your models here.

class Plant(models.Model):
    class DifficultyChoices(models.TextChoices):
        EASY = 'Easy',"Easy"
        MEDIUM = 'Medium',"Medium"
        HARD = 'Hard',"Hard"

    scientific_name = models.CharField(
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-zА-Яа-я]+ [A-Za-zА-Яа-я]+$', )]
    )


    description = models.TextField(
        max_length=500,
        blank=True,
    )

    image_url = models.URLField(
        blank=True,
    )

    watering_interval = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(90)]
    )

    difficulty = models.CharField(
        max_length=100,
        choices=DifficultyChoices.choices
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.01),
                    MaxValueValidator(9999.99)]
    )

    date_added = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.scientific_name

    class Meta:
        ordering = ['scientific_name']