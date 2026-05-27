# bookings/forms.py
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["user_name", "user_email", "seats_booked"]

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop("event", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        user_email = cleaned_data.get("user_email")
        seats_booked = cleaned_data.get("seats_booked")

        if not self.event:
            return cleaned_data

        if Booking.objects.filter(event=self.event, user_email=user_email).exists():
            raise forms.ValidationError(
                {"user_email": "Вы уже зарегистрированы на это мероприятие с таким Email."}
            )

        if seats_booked and seats_booked > self.event.available_seats:
            raise forms.ValidationError(
                {
                    "seats_booked": f"Нельзя взять больше мест, чем осталось! Доступно мест: {self.event.available_seats}."
                }
            )

        return cleaned_data
