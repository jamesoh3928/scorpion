from django.urls import path
from .views import vacation

urlpatterns = [
    path('', vacation, name='vacation')
]