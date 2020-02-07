from django.db import models

# Create your models here.


class news(models.Model):
    title = models.TextField()
    description = models.TextField()
    date = models.DateField()
    