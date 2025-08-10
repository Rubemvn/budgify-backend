from utils.db_utils import dictfetchall
from django.db import connection


class UsersRepository():
    
    def find_all(self):
        SQL = """SELECT * FROM users;"""
        
        with connection.cursor() as cursor:
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
        
        with connection.cursor() as cursor:
            cursor.execute(SQL, params)
            data = dictfetchall(cursor)
            
        return data[0] if data else {}
        