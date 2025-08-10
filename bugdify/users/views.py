from rest_framework import viewsets, status
from rest_framework.response import Response
from .repository import find_all

class UsersViewSet(viewsets.ViewSet):
    def list(self, request):
        # data = find_all()
        return Response('ok', status=status.HTTP_200_OK)