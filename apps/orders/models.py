from django.db import models


class Supplies(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='supplies/%Y/%m/%d')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
