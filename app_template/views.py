from rest_framework import viewsets
from rest_framework.response import Response
from .repository import find_all

class MyViewSet(viewsets.ViewSet):
    def list(self, request):
        data = find_all()
        return Response(data)