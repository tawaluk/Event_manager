from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import Group, UserAdmin

from .models import CustomUser

admin.site.unregister(Group)  # Убираем видимость админки групп

@register(CustomUser)
class MyUserAdmin(UserAdmin):
    list_display = ('pk', 'username', 'email', 'first_name', 'last_name', 'phone_number')
    list_filter = ('username', 'email')
