from django.db import models

class Item (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    cost = models.DecimalField(decimal_places=2, max_digits=20)

