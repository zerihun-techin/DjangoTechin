from django.db import models

# Create your models here.

class shop(models.Model):
    
    iteam = models.TextField()
    price = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.price   