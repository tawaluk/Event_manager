from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import Group, UserAdmin

from .models import CustomUser


admin.site.unregister(Group)  # Убираю видимость админки групп


@register(CustomUser)
class MyUserAdmin(UserAdmin):

    list_display = (
        'pk', 'username', 'email', 'first_name',
        'last_name', 'phone_number', 'organizations_list'
        )
    list_filter = ('username', 'email', 'organizations')
    search_fields = (
        'username', 'email', 'first_name', 'last_name', 'phone_number',
        )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {
            'fields': (
                'first_name', 'last_name',
                'email', 'phone_number'
                )}),
        ('Organizations', {'fields': ('organizations',)}),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined'
                                        )}),
    )

    def organizations_list(self, obj):
        """
        в списке пользователей
        добавляет в графу первые 3 организации в списке.
        """

        organizations = obj.organizations.all()[:3]
        organizations_str = ", ".join(
            [str(organization) for organization in organizations]
            )
        if obj.organizations.count() > 3:
            organizations_str += " +"
        return organizations_str
