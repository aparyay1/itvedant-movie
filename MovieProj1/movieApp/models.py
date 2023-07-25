from django.db import models

# Create your models here.
class Movie(models.Model):
    rel_date=models.DateField()
    movname=models.CharField(max_length=30)
    actorname=models.CharField(max_length=30)
    actressname=models.CharField(max_length=30)
    rating=models.IntegerField()
