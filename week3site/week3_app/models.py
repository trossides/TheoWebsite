from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_number = models.CharField(max_length=6, help_text='Unique part number for reordering.')
    address = models.CharField(max_length=200, help_text='Postal address of customer.')
    phone = models.CharField(max_length=15, help_text='Daytime contact details of customer.')
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name