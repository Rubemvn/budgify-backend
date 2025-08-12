from bugdify.core.helpers.sql import dictfetchall, format_query_for_debugging
from django.db import connections


class UsersRepository():
    
    def find_all(self):
        SQL = """SELECT * FROM users;"""
        
        with connections['bugdify'].cursor() as cursor:
            cursor.execute(SQL)
            data = dictfetchall(cursor)
            
        return data if data else []
    
    
    def find_user(self, pk=None):
        SQL = """
                SELECT * 
                FROM users
                WHERE id = %(id)s;
            """
        
        params = {
            'id': pk
        }
        
        with connections['bugdify'].cursor() as cursor:
            cursor.execute(SQL, params)
            print(format_query_for_debugging(SQL, params))
            data = dictfetchall(cursor)
            
        return data[0] if data else {}
        