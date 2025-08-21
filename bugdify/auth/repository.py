from bugdify.core.helpers.sql import dictfetchall, format_query_for_debugging
from django.db import connections

class AuthRepository():

    def find_all(self):
        SQL = """SELECT 1;"""
        
        with connections['bugdify'].cursor() as cursor:
            print(format_query_for_debugging(SQL))
            cursor.execute(SQL)
            data = dictfetchall(cursor)
            return data if data else []
        