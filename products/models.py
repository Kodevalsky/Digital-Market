from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) #max length is required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField("", max_digits=5, decimal_places=2)
    summary = models.TextField()
    is_preorder = models.BooleanField(default=False)
    photo_name = models.TextField(null=False, default="placeholder")