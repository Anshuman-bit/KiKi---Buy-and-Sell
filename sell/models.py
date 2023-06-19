from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

OWNERSHIP_CHOICES = (
    ("1st ownership", "1st ownership"),
    ("2nd ownership", "2nd ownership"),
    ("3rd ownership", "3rd ownership"),
    ("Antique", "Antique"),
)

class Sell_product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_ownership = models.CharField(max_length=50, choices=OWNERSHIP_CHOICES)
    product_location = models.CharField(max_length=100)
    product_image = models.ImageField(default="")
    #contact_us = models.PositiveIntegerField(null=False, default=10)
    #email_us = models.EmailField(default='')

    def __str__(self):
        return self.product_name
    