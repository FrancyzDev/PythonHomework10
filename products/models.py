from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(
        max_length=200, 
        verbose_name="Назва товару"
    )
    image = models.ImageField(
        upload_to='products/', 
        verbose_name="Зображення продукту"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Ціна"
    )
    calories = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Калорiйнiсть"
    )