from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

class Libro (models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    sinopsys = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    edited_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
