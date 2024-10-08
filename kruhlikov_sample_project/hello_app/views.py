from django.http import HttpResponse


class View:
    @staticmethod
    def hello(request) -> HttpResponse:
        try:
            count_reload_page: int = request.session["count_reload_page"]
            count_reload_page += 1
            all_cookies: str = request.COOKIES
            request.session["count_reload_page"]: int = count_reload_page
            response: HttpResponse = HttpResponse(f'<div style="width: 100%; height: 100%; text-align: center; '
                                    f'background-color: #303030;"><h1 '
                                    f'style="color: white">Hello, '
                                    f'Sasha!</h1> <br><strong style="color: white; position: absolute; bottom: 20px; margin-left: -270px;'
                                    f'">All cookies: {all_cookies} <br>'
                                    f'Count reload '
                                    f'pag'
                                    f'e: {count_reload_page} </strong>'
                                    f"</div>")
            response.set_cookie("author", "Kruhlikov")
            return response
        except:
            request.session["count_reload_page"]: int = 0
            count_reload_page = 0
            all_cookies: str = request.COOKIES
            response: HttpResponse = HttpResponse(f'<div style="width: 100%; height: 100%; text-align: center; '
                                                  f'background-color: #303030;"><h1 '
                                                  f'style="color: white">Hello, '
                                                  f'Sasha!</h1> <br><strong style="color: white; position: absolute; bottom: 20px; margin-left: -270px;'
                                                  f'">All cookies: {all_cookies} <br>'
                                                  f'Count reload '
                                                  f'pag'
                                                  f'e: {count_reload_page} </strong>'
                                                  f"</div>")
            return response