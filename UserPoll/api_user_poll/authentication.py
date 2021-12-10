import datetime
from typing import Tuple

from django.conf import settings
from django.utils import timezone

from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from rest_framework.exceptions import AuthenticationFailed

from auth.models import Userauth


class ApiClientAuthentication(TokenAuthentication):
    keyword = "Token"
    model = Userauth
    error_message = "Клиент API с указанным токеном не существует."

    def authenticate_credentials(self, token: str):
        try:
            user_token = Userauth.objects.get(token=token)
            print(user_token)
        except Userauth.DoesNotExist:
            raise exceptions.AuthenticationFailed(self.error_message)

        if timezone.now() >= user_token.created_at + datetime.timedelta(seconds=settings.TOKEN_EXPIRATION_HOURS * 3600):
            raise AuthenticationFailed('Аутентификационная сессия истекла.')

        return user_token,None
