from django.urls import path
from .views import SuppliesList


urlpatterns = [
    path('supplies/', SuppliesList.as_view(), name = 'supplies_list'),
]