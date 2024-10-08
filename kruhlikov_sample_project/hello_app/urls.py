from .views import View
from django.urls import path

urlpatterns = [
    path("", View.hello, name="hello")
]