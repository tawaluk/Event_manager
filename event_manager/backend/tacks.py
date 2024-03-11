from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import Event


@shared_task
def create_event(event_data):
    Event.objects.create(**event_data)


@shared_task
def create_event_with_delay(event_data):
    create_event.apply_async(
        args=[event_data], eta=timezone.now() + timedelta(seconds=60)
        )
