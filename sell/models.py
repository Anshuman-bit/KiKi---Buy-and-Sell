from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models import ForeignKey

# Create your models here.

OWNERSHIP_CHOICES = (
    ("1st ownership", "1st ownership"),
    ("2nd ownership", "2nd ownership"),
    ("3rd ownership", "3rd ownership"),
    ("Antique", "Antique"),
)


class Sell_product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_ownership = models.CharField(max_length=50, choices=OWNERSHIP_CHOICES, null=False)
    product_location = models.CharField(max_length=100)
    product_image = models.ImageField(default="")
    contact_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], default='')

    # email_address = models.EmailField( max_length=254)

    def __str__(self):
        return self.product_name

    def __dir__(self):
        return self.user
