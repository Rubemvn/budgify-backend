from rest_framework import viewsets, status
from rest_framework.response import Response
from bugdify.users.repository import UsersRepository


class UsersViewSet(viewsets.ViewSet):
    def list(self, request):
        repo = UsersRepository()
        
        try:
            data = repo.find_all()
            return Response(data, status=status.HTTP_200_OK)\
                
        except Exception as e:
            print("Error...:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def retrieve(self, request, pk=None):
        
        repo = UsersRepository()
        
        try:
            data = repo.find_user(pk)
            return Response(data, status=status.HTTP_200_OK)
        
        except Exception as e:
            print("Error...:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
