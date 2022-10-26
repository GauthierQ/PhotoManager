from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField()