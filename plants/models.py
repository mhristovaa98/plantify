from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models

# Create your models here.

class Plant(models.Model):
    class DifficultyChoices(models.TextChoices):
        EASY = 'Easy',"Easy"
        MEDIUM = 'Medium',"Medium"
        HARD = 'Hard',"Hard"

    class LocationChoices(models.TextChoices):
        LIVING_ROOM = 'Living Room',"Living Room"
        BEDROOM = 'Bedroom',"Bedroom"
        KITCHEN = 'Kitchen',"Kitchen"
        BATHROOM = 'Bathroom',"Bathroom"
        BALCONY = 'Balcony',"Balcony"
        GARDEN = 'Garden',"Garden"

    class LightRequirementChoices(models.TextChoices):
        LOW_LIGHT = 'Low Light',"Low Light"
        MEDIUM_INDIRECT_LIGHT = 'Medium Indirect Light',"Medium Indirect Light"
        HIGH_INDIRECT_LIGHT = 'High Indirect Light', "High Indirect Light"
        DIRECT_LIGHT = 'Direct Light',"Direct Light"

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
    location = models.CharField(

        max_length=30,
        choices=LocationChoices.choices,
    )

    light_requirement = models.CharField(

        max_length=30,
        choices=LightRequirementChoices.choices,
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