from django.urls import path, re_path
from . import views

urlpatterns = [
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    re_path(
        r"^cancel/(?P<booking_id>\d+)/$", views.cancel_booking, name="cancel_booking"
    ),
]
