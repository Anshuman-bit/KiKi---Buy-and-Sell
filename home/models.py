from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


# Create your models here

class Home(models.Model):
    contact_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    email_address = models.EmailField(max_length=254)

    def __str__(self):
        return self.email_address

# class Kiki_user(models.Model):
