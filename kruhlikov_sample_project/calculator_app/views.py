from django.shortcuts import render


class View:
    @staticmethod
    def calc(request):
        buttons: dict[str, list[str]] = {
          "row1": ["7", "8", "9", 'x', "C"],
          "row2": ["4", "5", "6", "-", '/'],
          "row3": ["1", "2", "3", "+"],
          "row4": [".", "0", "<=", ]
        }
        if request.method == 'POST':
            solution: str = request.POST.get('solution')
            if "x" in solution:
                solution: str = solution.replace("x", "*")
            try:
                res = eval(solution)
            except:
                res = "ERROR"
            return render(request, "calculator_app/calculator.html", {"solution": res, "data": buttons})
        return render(request, 'calculator_app/calculator.html', {"data": buttons})