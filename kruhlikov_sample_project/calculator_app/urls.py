from .views import View
from django.urls import path

urlpatterns = [
    path("", View.calc, name="calc")
]