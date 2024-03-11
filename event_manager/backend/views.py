from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from django_filters import rest_framework as django_filters
from django.core import serializers as dj

from .models import Event, Organization
from .serializers import OrganizationSerializer, EventSerializer
from .filters import EventFilter
from .tacks import create_event_with_delay


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = EventFilter
    search_fields = ['title']
    ordering_fields = ['date']
    pagination_class = LimitOffsetPagination


class OrganizationViewSet(viewsets.ModelViewSet):

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
