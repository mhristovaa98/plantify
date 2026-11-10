from django.db import models

# Create your models here.
class Collection(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    description = models.TextField(
        blank=True,
        max_length=300,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    plants = models.ManyToManyField(
        'plants.Plant',
    )

    def __str__(self):
        return self.name
