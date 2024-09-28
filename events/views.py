from .models import Event, EventCategory
from django.shortcuts import render, get_object_or_404


def events_list(request):
    category = request.GET.get('category')
    if category is not None:
        events = Event.objects.filter(category__slug=category).order_by("-pk")
    else:
        events = Event.objects.order_by("-pk")

    active_category = request.GET.get('category', None)
    context = {
        "title_tag": "Events",
        'category_name': "All",
        "events": events,
        "active_category": active_category,
        "categories": EventCategory.objects.all(),
    }
    return render(request, "events_list.html", context)


def event_detail(request, slug, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {
        "title_tag": event.name,
        "event": event,
        "upcoming_events": Event.objects.order_by("-pk"),
    }
    return render(request, "event_detail.html", context)


def search_events(request):
    context = {
        "title_tag": f'"{request.GET.get("q")}" results',
    }
    return render(request, "events_list.html", context)
