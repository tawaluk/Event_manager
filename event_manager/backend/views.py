from rest_framework import filters, generics
from .models import Event
from .serializers import EventSerializer


class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date']
    search_fields = ['title']
    # pagination_class = LimitOffsetPagination