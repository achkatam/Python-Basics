from django.db import models


class Drink(models.Model):
    name_of_product = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name_of_product} - {self.description} - ${self.price}"
