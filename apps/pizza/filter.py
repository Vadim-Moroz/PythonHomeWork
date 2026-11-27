from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.pizza.models import PizzaModel

# Фільтрує отримані дані за запитом
def filter_pizza(query:QueryDict)->QuerySet:
    # Отримує дані
    qs=PizzaModel.objects.all()
    # Перебирає ключі та значення параметрів запиту
    for k,v in query.items():
        # Визначає який тип фільтрації треба виконати
        match k:
            case "price_gt":
                # Фільтрує за ціною більше зазначеної
                qs=qs.filter(price__gt=v)
            case "price_lt":
                # Фільтрує за ціною менше зазначеної
                qs=qs.filter(price__lt=v)
                # Генерує помилку у випадку відсутності доступної фільтрації
            case _:
                raise ValidationError(f"Pizza {k} is not valid")
    # Повертає відфільтрований масив даних
    return qs

