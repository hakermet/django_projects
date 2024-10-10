from django.shortcuts import render


class View:
    @staticmethod
    def guess(request):
        if request.method == 'POST':
            guess = int(request.POST.get('guess'))
            secret_number = 50
            if guess == secret_number:
                return render(request, 'guess_game_app/random_number.html', {'result': 'You win ', "current_number":
                    guess, "class": "win"})
            elif guess < secret_number:
                return render(request, 'guess_game_app/random_number.html', {'result': 'Too low! Try again.',
                                                                     "current_number": guess, "class": "lose"})
            else:
                return render(request, 'guess_game_app/random_number.html', {'result': 'Too high! Try again.',
                                                                     "current_number": guess,
                                                                     "class": "lose"})
        else:
            return render(request, 'guess_game_app/random_number.html')