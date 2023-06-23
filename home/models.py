from django.db import models
from django.core.validators import RegexValidator
# Create your models here

class Home(models.Model):
    contact_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    email_address = models.EmailField( max_length=254)
    
    def __str__(self):
        return self.email_address
    