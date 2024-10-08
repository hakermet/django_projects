
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home_app.urls")),
    path("calc/", include('calculator_app.urls')),
    path("hello/", include('hello_app.urls')),
    path("guess/", include('guess_game_app.urls'))
]