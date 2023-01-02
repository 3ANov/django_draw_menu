from django.db import connection


class SqlQueryCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print(str(len(connection.queries)) + " queries")
        return response
