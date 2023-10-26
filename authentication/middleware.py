from django.core.cache import cache
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import UntypedToken

class ExpireTokenOnRoleChangeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the user is authenticated and the role has changed
        if request.user.is_authenticated and request.user.has_role_changed():
            # Expire the access token
            self.expire_access_token(request.user)

        return response

    def expire_access_token(self, user):
        # Get the user's access token from cache
        cache_key = f'user_token:{user.id}'
        token_data = cache.get(cache_key)

        if token_data:
            # Expire the access token
            token = UntypedToken(token_data['access_token'])
            token.set_exp(lifetime=0)  # Set the expiration to the past
            cache.set(cache_key, token_data, timeout=0)

    def process_response(self, request, response):
        return response
