from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import MyViewSet

router = SimpleRouter()
router.register(r'example', MyViewSet, basename='example')

urlpatterns = [
    path('', include(router.urls)),
]