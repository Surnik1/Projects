from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from bookings.forms import BookingForm


def event_list(request):
    events = Event.objects.all()
    date_filter = request.GET.get("date")
    if date_filter:
        events = events.filter(date__date=date_filter)
    return render(request, "events/list.html", {"events": events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        form.instance.event = event

        if form.is_valid():
            booking = form.save()

            event.available_seats -= booking.seats_booked
            event.save()

            return redirect("my_bookings")
    else:
        form = BookingForm()

    return render(request, "events/detail.html", {"event": event, "form": form})
