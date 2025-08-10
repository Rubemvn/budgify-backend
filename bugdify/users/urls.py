from django.urls import path, include
from rest_framework.routers import SimpleRouter
from bugdify.users.views import UsersViewSet

router = SimpleRouter()
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]