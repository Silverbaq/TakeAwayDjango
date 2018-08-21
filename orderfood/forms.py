from django import forms
from datetimewidget.widgets import DateTimeWidget
from django.utils.timezone import now

from .models import Event, Order, OrderLine


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['name', 'start_at', 'end_at', 'key', 'location']
        widgets = {
            'start_at': forms.DateTimeInput(attrs={'class': 'datetimepicker'}),
            'end_at': forms.DateTimeInput(attrs={'class': 'datetimepicker'}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['when', 'order_from', 'transport_price']
        widgets = {
            'when': forms.DateTimeInput(attrs={'class': 'datetimepicker'}),
        }


class OrderLineForm(forms.ModelForm):
    class Meta:
        model = OrderLine
        fields = ['name', 'price']
