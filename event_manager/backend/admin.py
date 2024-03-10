from django.contrib import admin
from django.contrib.admin import register, ModelAdmin
from django.contrib.auth.admin import UserAdmin

from .models import Event, Organization


@register(Event)
class EventAdmin(ModelAdmin):
    """Отображение модели ивентов в админке."""

    list_display = ("title", "description", "get_organizations", "date")
    search_fields = ("title", "date")
    list_filter = ("title", "date")

    def get_organizations(self, obj):
        """Отображение названий организваций в ивентах. Для удобства."""

        return ", ".join([org.title for org in obj.organizations.all()])
    get_organizations.short_description = "Organizations"


@register(Organization)
class OrganizationAdmin(ModelAdmin):

    list_display = ("title", "description", "address", "postcode")
    search_fields = ("title", "address")
    list_filter = ("title", "address")

