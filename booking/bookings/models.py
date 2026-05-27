from django.db import models
from events.models import Event


class Booking(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="bookings",
        verbose_name="Мероприятие",
    )
    user_name = models.CharField(max_length=100, verbose_name="Имя")
    user_email = models.EmailField(verbose_name="Email")
    seats_booked = models.PositiveIntegerField(verbose_name="Забронировано мест")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.event.name}"

    class Meta:

        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
