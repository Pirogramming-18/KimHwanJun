from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=32)
    year = models.IntegerField()
    genre = models.CharField(max_length=16)
    rate = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(5.0)])
    runningtime = models.CharField(max_length=8)
    content = models.TextField()
    director = models.CharField(max_length=16)
    act = models.CharField(max_length=16)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


