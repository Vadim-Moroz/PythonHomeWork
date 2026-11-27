from django.db import models

# Базова модель яка використовується іншими моделями
class BaseModel(models.Model):
    class Meta:
        # Визначення класу як абстрактний
        abstract = True
    # атрибути абстрактного класу які будуть мати всі класи які наслідують цей клас
    # Дата та час створення об'єкта
    created_at = models.DateTimeField(auto_now_add=True)
    # Дата та час останнього збереження об'єкта
    updated_at = models.DateTimeField(auto_now=True)