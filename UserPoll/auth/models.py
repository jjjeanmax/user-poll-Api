from django.db import models

import uuid


class Userauth(models.Model):

    user_id = models.IntegerField(unique=True, editable=True)
    username = models.CharField(max_length=512, verbose_name='ФИО', blank=True)
    token = models.UUIDField(primary_key=True, verbose_name='токен', default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        verbose_name = "Токен пользователя"
        verbose_name_plural = "Токены пользователей"

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True
