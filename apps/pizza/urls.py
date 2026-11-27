from django.urls import path
from apps.pizza.views import PizzaListCreateView,PizzaRetrieveUpdateDestroyView

# Шляхи які використовуються для надсилання HTTP-запитів
urlpatterns = [
    # Запити для класу PizzaListCreateView
    path('',PizzaListCreateView.as_view()),
    # Запити для класу PizzaRetrieveUpdateDestroyView з використанням ідентифікатора
    path('/<int:pk>',PizzaRetrieveUpdateDestroyView.as_view()),
]