from django.db import models
from django.conf import settings

# Create your models here.


class UserCart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # items = models.ManyToManyField(Product)
    # price = models.FloatField(validators=[MinValueValidator(0)], default=0)
