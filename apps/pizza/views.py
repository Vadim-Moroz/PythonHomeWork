from typing import Any

from django.db.models import Q, Min, Max, Count, QuerySet
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveDestroyAPIView

from apps import pizza
from apps.pizza.filter import filter_pizza
from apps.pizza.serialazers import PizzaSerializers
from apps.pizza.models import PizzaModel
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin

# клас для отримання списку записів та створення нових записів
# class PizzaListCreateView(APIView):
#
        # отримує всі дані
#     def get(self,request:Request, *args, **kwargs):
             # отримує дані з бази даних
#         qs=PizzaModel.objects.all()
             # отримує дані з бази даних відповідно до зазначених фільтрів
#         # pizzas=PizzaModel.objects.filter(Q(size__gt=5)|Q(name='')&Q()).exclude(size=310).order_by('price','size').reverse()
             # отримує певну кількість даних з бази даних
#           pizzas=PizzaModel.objects.all()[:2]
             # отримує певні поля даних
#         # pizzas=PizzaModel.objects.all().values('id','name','price')
             # визначає максимальне та мінімальне значення даних price
#         # agregete=PizzaModel.objects.aaggregate(Min('price'),Max('price'))
             # групує записи за size та підраховує їх кількість
#         # anotate=PizzaModel.objects.values('size').annotate(count=Count('size'))
#         # print(anotate)
             # викликає метод для фільтрування даних за параметром
#         qs=filter_pizza(request.query_params)
             # створює серіалізатора PizzaSerializers з даними (qs)
#         serializer=PizzaSerializers(qs,many=True)
             # повертає дані зі статусом HTTP 200
#         return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response("od")
#
             # додає новий запис в базі даних
#     def post(self,request, *args, **kwargs):
             # створює серіалізатора PizzaSerializers з новими переданими користувачем даними (request.data)
#         serializer= PizzaSerializers(data=request.data)
             # валідує дані або генерує помилку якщо дані не пройшли валідацію
#         serializer.is_valid(raise_exception=True)
             # записує дані та зберігає зміни
#         serializer.save()
             # Повертає створений об'єкт зі статусом HTTP 201
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# Клас для отримання, оновлення та видалення запису за ідентифікатором
# class PizzaRetrieveUpdateDestroyView(APIView):
        # отримує певний запис за відповідним ідентифікатором
#     def get(self, request, *args, **kwargs):
            # отримує з запиту значення ідентифікатора з URL
#         pk=kwargs['pk']
            # виконує блок коду, у якому може виникнути виняток
#         try:
                # отримує запис із бази даних за ідентифікатором
#             pizzas=PizzaModel.objects.get(pk=pk)
            # якщо запит повертає помилку то except ловить її та виконує зазначену дію
#         except PizzaModel.DoesNotExist:
            # повертає відповідний текст та статус 404
#             return Response({'details' : 'Not found'},status=status.HTTP_404_NOT_FOUND)
            # створює серіалізатора PizzaSerializers з даними (pizzas)
#         serializer= PizzaSerializers(instance=pizzas, many=False)
            # повертає дані зі статусом HTTP 200
#         return Response(serializer.data, status=status.HTTP_200_OK)

        # змінює відповідний запис
#     def put(self, request, *args, **kwargs):
            # отримує з запиту значення ідентифікатора з URL
#         pk=kwargs['pk']
            # виконує блок коду, у якому може виникнути виняток
#         try:
                # отримує запис із бази даних за ідентифікатором
#             pizzas=PizzaModel.objects.get(pk=pk)
#         except PizzaModel.DoesNotExist:
                # повертає відповідний текст та статус 404
#             return Response({'details' : 'Not found'},status=status.HTTP_404_NOT_FOUND)
            # створює серіалізатора PizzaSerializers з старими даними (pizzas) та новими переданими користувачем даними (request.data)
#         serializer= PizzaSerializers(instance=pizzas, data=request.data)
            # валідує дані
#         serializer.is_valid(raise_exception=True)
            # записує дані та зберігає зміни
#         serializer.save()
            # повертає дані зі статусом HTTP 200
#         return Response(serializer.data, status=status.HTTP_200_OK)

        # видаляє відповідний запис
#     def delete(self, request, *args, **kwargs):
            # отримує з запиту значення ідентифікатора з URL
#         pk=kwargs['pk']
            # виконує блок коду, у якому може виникнути виняток
#         try:
                # отримує запис із бази даних за ідентифікатором та видаляє його
#             PizzaModel.objects.get(pk=pk).delete()
#         except PizzaModel.DoesNotExist:
                # повертає відповідний текст та статус 404
#             return Response({'details' : 'Not found'},status=status.HTTP_404_NOT_FOUND)
                # при успішному видалені повертає статус 204
#         return Response(status=status.HTTP_204_NO_CONTENT)

# клас для отримання списку записів та створення нових записів
# class PizzaListCreateView(GenericAPIView,ListModelMixin,CreateModelMixin):
        # отримує дані з бази даних
#     # queryset = PizzaModel.objects.all()
        # визначає клас серіалізатора
#     serializer_class = PizzaSerializers
#
        # метод отримання записів з бази даних
#     def get_queryset(self):
            # отримує записи
#         request:Request=self.request
            # фільтрує за допомогою метода filter_pizza та повертає записи
#         return filter_pizza(request.query_params)
#
        # отримує записи за допомогою методу list із класу ListModelMixin
#     def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
#         return super().list(request, *args, **kwargs)
#
        # створює записи за допомогою методу create із класу CreateModelMixin
#     def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
#         return super().create(request, *args, **kwargs)

        # отримує всі дані
    # def get(self, request: Request, *args, **kwargs):
            # викликає метод для фільтрування даних за параметром
    #     qs=filter_pizza(request.query_params)
            # створює серіалізатора PizzaSerializers з даними (qs)
    #     serializer=PizzaSerializers(qs,many=True)
            # повертає дані зі статусом HTTP 200
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
        # додає новий запис в базі даних
    # def post(self, request, *args, **kwargs):
            # створює серіалізатора PizzaSerializers з новими переданими користувачем даними (request.data)
    #     serializer= PizzaSerializers(data=request.data)
            # валідує дані або генерує помилку якщо дані не пройшли валідацію
    #     serializer.is_valid(raise_exception=True)
            # записує дані та зберігає зміни
    #     serializer.save()
            # Повертає створений об'єкт зі статусом HTTP 201
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

# Клас для отримання, оновлення та видалення запису за ідентифікатором
# class PizzaRetrieveUpdateDestroyView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#
        # отримує дані з бази даних
#     queryset=PizzaModel.objects.all()
        # визначає клас серіалізатора
#     serializer_class = PizzaSerializers

        # отримує записи за ідентифікатором за допомогою методу retrieve із класу RetrieveModelMixin
#     def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
#         return super().retrieve(request, *args, **kwargs)
#
# оновлює записи за допомогою методу update із класу UpdateModelMixin
#     def put(self, request: Request, *args: Any, **kwargs: Any) -> Response:
#         return super().update(request, *args, **kwargs)
#
# частково оновлює записи за допомогою методу partial_update із класу UpdateModelMixin
#     def patch(self, request: Request, *args: Any, **kwargs: Any) -> Response:
#         return super().partial_update(request, *args, **kwargs)
#
# видаляє запис за допомогою методу destroy із класу DestroyModelMixin
#     def delete(self, request: Request, *args: Any, **kwargs: Any) -> Response:
#         return super().destroy(request, *args, **kwargs)

# клас для отримання списку записів та створення нових записів
class PizzaListCreateView(ListCreateAPIView):
    # queryset = PizzaModel.objects.all()
    serializer_class = PizzaSerializers

    # метод отримання записів з бази даних
    def get_queryset(self):
        # отримує записи
        request:Request=self.request
        # фільтрує за допомогою метода filter_pizza та повертає записи
        return filter_pizza(request.query_params)

# клас для отримання, оновлення та видалення запису за ідентифікатором
class PizzaRetrieveUpdateDestroyView(RetrieveDestroyAPIView):
    # отримує дані з бази даних
    queryset=PizzaModel.objects.all()
    # визначає клас серіалізатора
    serializer_class = PizzaSerializers
    # визначає які методи доступні в цьому класі
    http_method_names = ['get','post','put','delete']