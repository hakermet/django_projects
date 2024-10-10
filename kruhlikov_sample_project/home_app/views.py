from django.shortcuts import render


class View:
    @staticmethod
    def home(request):
        return render(request, 'home_app/home.html')