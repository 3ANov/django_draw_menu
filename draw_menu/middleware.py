from datetime import datetime

from django.db import connection


class SqlQueryCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        now = datetime.now()
        count_queries = str(len(connection.queries))
        print(f"{count_queries} queries in {now}")
        return response
