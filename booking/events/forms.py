from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["user_name", "user_email", "seats_booked"]

    def clean(self):
        cleaned_data = super().clean()
        user_email = cleaned_data.get("user_email")
        seats_booked = cleaned_data.get("seats_booked")

        event = self.instance.event

        if event and user_email:
            duplicate_exists = Booking.objects.filter(
                event=event, user_email=user_email
            ).exists()

            if duplicate_exists:
                self.add_error(
                    "user_email", "Вы уже забронировали места на это мероприятие!"
                )
        if seats_booked is not None and seats_booked <= 0:
            self.add_error("seats_booked", "Количество мест должно быть больше нуля!")
        if event and seats_booked:
            if seats_booked > event.available_seats:
                self.add_error(
                    "seats_booked",
                    f"Недостаточно мест! Осталось: {event.available_seats}",
                )

        return cleaned_data
