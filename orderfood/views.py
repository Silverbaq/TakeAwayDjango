from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event, Order
from .forms import EventForm, OrderForm, OrderLineForm


# Create your views here.
def home(request):
    events = Event.objects.all()
    return render(request, 'orderfood/home.html', {'events': events})


@login_required
def create_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        event = form.save(commit=False)
        event.save()
        return redirect('event', pk=event.pk)
    return render(request, 'orderfood/create_event.html', {'form': form})


def show_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'orderfood/event.html', {'event': event})


def create_order(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = OrderForm(request.POST or None)
    if form.is_valid():
        order = form.save(commit=False)
        order.event = event
        order.starter = request.user
        order.save()
        return redirect('event', pk=pk)
    return render(request, 'orderfood/create_order.html', {'event': event, 'form': form})


def show_order(request, event_pk, order_pk):
    event = get_object_or_404(Event, pk=event_pk)
    order = get_object_or_404(Order, pk=order_pk)
    return render(request, 'orderfood/order.html', {'event': event, 'order': order})