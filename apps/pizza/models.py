from django.db import models

from apps.core.models import BaseModel

# Модель продукту що наслідує абстрактний клас BaseModel
class PizzaModel(BaseModel):
    # Задає назву таблиці
    class Meta:
        db_table = 'pizza'
    # Назва продукту максимальна довжина якої 20 символів
    name = models.CharField(max_length=20)
    # Розмір продукту
    size = models.IntegerField()
    # Ціна продукту
    price = models.FloatField()
