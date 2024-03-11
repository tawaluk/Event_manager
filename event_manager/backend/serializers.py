from rest_framework import serializers

from .models import Event, Organization
from users.models import CustomUser
from users.serializers import UserSerializer


class OrganizationSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()
    title = serializers.CharField()
    postcode = serializers.CharField()
    address = serializers.CharField()

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'postcode': instance.postcode,
            'address': instance.address
        }

    class Meta:
        model = Organization
        fields = ['id', 'title', 'postcode', 'address']


class EventSerializer(serializers.ModelSerializer):

    class Meta:

        model = Event
        fields = [
            'id', 'title', 'description',
            'date', 'organizations', 'image'
            ]

    def to_representation(self, instance):

        representation = super().to_representation(instance)
        organizations = instance.organizations.all()
        representation['organizations'] = [
            OrganizationSerializer(org).data for org in organizations
            ]
        users = CustomUser.objects.filter(organizations__in=organizations)
        representation['users'] = UserSerializer(users, many=True).data

        return representation
