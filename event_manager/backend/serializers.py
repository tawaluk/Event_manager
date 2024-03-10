from rest_framework import serializers
from .models import Event, Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def to_representation(self, instance):
        """Возвращает названия орагнизаций, участвующих в ивенте."""
        representation = super().to_representation(instance)
        organizations = instance.organizations.all()
        representation['organizations'] = [org.title for org in organizations]
        return representation
