from rest_framework import serializers

from .models import Event, Organization
from users.models import CustomUser
from users.serializers import UserSerializer


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ['id', 'title', 'postcode', 'address']


class EventSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = Event
        fields = ['id', 'title', 'description','date', 'organizations', 'image']

    def to_representation(self, instance):
        """Возвращает названия и идентификаторы организаций, участвующих в ивенте."""

        representation = super().to_representation(instance)
        
        organizations = instance.organizations.all()
        representation['organizations'] = OrganizationSerializer(organizations, many=True).data
        
        users = CustomUser.objects.filter(organizations__in=organizations)
        representation['users'] = UserSerializer(users, many=True).data

        return representation
