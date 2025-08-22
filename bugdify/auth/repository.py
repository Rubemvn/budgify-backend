from bugdify.core.helpers.sql import dictfetchall, format_query_for_debugging
from django.db import connections

class AuthRepository():
    
    def find_user(self, username: str)-> bool:
        
        SQL = """SELECT id FROM users WHERE username = %s"""
        
        with connections['bugdify'].cursor() as cursor:
            print(format_query_for_debugging(SQL, (username,)))
            cursor.execute(SQL, (username,))
            data = dictfetchall(cursor)
            return data[0] if data else False

    def authentication_user(self, data_user: object) -> bool:
        SQL = """
            SELECT 
                u.id,
                u.username,
                u.email,
                u.first_name,
                u.last_name,
                u.is_active,
                u.date_joined,
                u.last_login,
                u.updated_at
            FROM users u
            WHERE username = %(username)s
            AND password_hash = %(password)s;"""
        
        with connections['bugdify'].cursor() as cursor:
            print(format_query_for_debugging(SQL, data_user))
            cursor.execute(SQL, data_user)
            data = dictfetchall(cursor)
            return data[0] if data else False
        