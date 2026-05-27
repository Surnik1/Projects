from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking


def my_bookings(request):
    email = request.GET.get("email", "").strip()

    bookings = None
    if email:
        bookings = Booking.objects.filter(user_email=email)
    context = {"bookings": bookings, "email": email}
    return render(request, "bookings/my_bookings.html", context)


def cancel_booking(request, booking_id):
    if request.method == "POST":
        booking = get_object_or_404(Booking, id=booking_id) 
        event = booking.event

        event.available_seats += booking.seats_requested
        event.save()

        booking.delete()
    return redirect("my_bookings")
