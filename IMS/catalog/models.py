from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    quantity = models.IntegerField(default=0,null=False)
    is_rentable = models.BooleanField(default=True, null=False)
    rental_rate = models.IntegerField(default=0, null=False)
    member_rate = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to="product_images/",blank=True,null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name