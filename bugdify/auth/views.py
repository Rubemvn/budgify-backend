from rest_framework import viewsets, status
from rest_framework.response import Response
from bugdify.auth.repository import AuthRepository

class AuthViewSet(viewsets.ViewSet):
    def list(self, request):
        
        repo = AuthRepository()
        
        try:
            data = repo.find_all()
            return Response(data, status=status.HTTP_200_OK)
        
        except Exception as e:
            print("Error...:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)