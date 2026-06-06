from django.db import models
from django.core.validators import MinLengthValidator

class Branch(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Назва філії"
    )
    address = models.CharField(
        max_length=300,
        verbose_name="Адреса"
    )
    phone = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(9)],
        verbose_name="Телефон"
    )
    work_hours = models.CharField(
        max_length=100,
        default="10:00 - 22:00",
        verbose_name="Години роботи"
    )
    special = models.TextField(
        blank=True,
        verbose_name="Особливості/Спецпропозиції"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Філія"
        verbose_name_plural = "Філії"
        ordering = ['name']