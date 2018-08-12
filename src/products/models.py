from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    summary = models.TextField(blank=True, null=False)
    contact_mail = models.EmailField()
    post_date = models.DateField(auto_now=True)
    feature = models.BooleanField()
