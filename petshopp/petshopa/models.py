from django.db import models

class PetShop(models.Model):
        name = models.CharField(max_length=50)
        age = models.IntegerField()
        available = models.BooleanField(default=True)
        price = models.DecimalField(max_digits=5, decimal_places=2,)
        image = models.ImageField(blank=True,null=True)
