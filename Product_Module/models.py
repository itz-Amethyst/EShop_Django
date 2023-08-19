from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 200)
    price = models.IntegerField()
    rating = models.IntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(5)], default = 0
    )
    short_description = models.CharField(max_length = 360, null = True)
    is_active = models.BooleanField(null = True)

    def __str__(self):
        return f"{self.title} ({self.price})"
