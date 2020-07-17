from django.urls import path, include
from .views import Articles


urlpatterns = [
    path('', Articles, name = "Articles"),
]