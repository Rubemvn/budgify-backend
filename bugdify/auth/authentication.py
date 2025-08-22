from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from bugdify.auth.blacklist_cache import is_blacklisted

class JWTAuthWithMemoryBlacklist(JWTAuthentication):
    def authenticate(self, request):
        result = super().authenticate(request)
        if result is None:
            return None

        user, token = result
        jti = token.get("jti")
        if is_blacklisted(jti):
            raise AuthenticationFailed("Token inválido (blacklist)")

        return (user, token)
