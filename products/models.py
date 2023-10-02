from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) #max length is required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField("", max_digits=5, decimal_places=2)
    summary = models.TextField()
    is_preorder = models.BooleanField(default=False)
    photo_name = models.TextField(null=False, default="placeholder")

class CartItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    attribute1 = models.CharField(choices=[(1, "Texas Tea"), (2, "Fiesta Red"), (3,"Cobalt Blue")], max_length=64)
    attribute2 = models.CharField(choices=[(1, "XS"), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL')], max_length=64)