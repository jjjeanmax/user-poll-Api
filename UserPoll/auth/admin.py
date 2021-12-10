from django.contrib import admin

from .models import Userauth


@admin.register(Userauth)
class AuthorizationAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'token','created_at','username')
