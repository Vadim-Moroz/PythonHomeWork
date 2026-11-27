
from rest_framework import serializers

from apps.pizza.models import PizzaModel


# Клас який валідує отримані дани
class PizzaSerializers(serializers.ModelSerializer):
    # Визначає модель та поля які має ця модель
    # Також виконує всі методи: створення, оновлення і тд без необхідності їх написання
    class Meta:
        model = PizzaModel
        fields = ('id','name','size','price','created_at','updated_at')
        # Використання всіх полів моделі
        # fields = '__all__'

    # read_only=True означає, що поле доступне лише для читання і не може бути змінене через вхідні дані
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=20)
    # size = serializers.IntegerField()
    # price = serializers.FloatField()
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)

    # Метод для створення об'єкта при валідних даних
    # def create(self, validated_data):
    #     return PizzaModel.objects.create(**validated_data)

    # Метод для оновлення існуючого об'єкта при валідних даних
    # def update(self, instance, validated_data:dict):
    #     for k,v in validated_data.items():
    #         setattr(instance, k, v)
    #     instance.save()
    #     return instance