from utils.db_utils import dictfetchall
from django.db import connection

class MyAppRepository():

    def find_all(self):
        SQL = """SELECT 1;"""
        
        with connection.cursor() as cursor:
            cursor.execute(SQL)
            data = dictfetchall(cursor)
            return data if data else []
        