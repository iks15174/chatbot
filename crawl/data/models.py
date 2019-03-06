from django.db import models

class youtube(models.Model):
    title = models.CharField(max_length=200)
    author =  models.CharField(max_length=200)
    link = models.URLField()
# Create your models here.
