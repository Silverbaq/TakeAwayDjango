from django.db import models
from django.conf import settings

# Create your models here.
from django.db.models import CASCADE
from django.utils.timezone import now


class Event(models.Model):
    name = models.CharField(max_length=50, unique=True)
    start_at = models.DateTimeField(null=False, blank=False, default=now)
    end_at = models.DateTimeField(null=False, blank=False, default=now)
    key = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_from = models.CharField(max_length=300, null=False)
    starter = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name='orders_started', on_delete=CASCADE)
    when = models.DateTimeField(null=False, blank=False, default=now)
    transport_price = models.PositiveIntegerField()
    event = models.ForeignKey(Event, related_name='orders', on_delete=CASCADE)

    def __str__(self):
        return "{0}\t{1}".format(self.order_from, self.when)


class OrderLine(models.Model):
    by = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name='orders', on_delete=CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    price = models.PositiveIntegerField()
    order = models.ForeignKey(Order, related_name='order_lines', on_delete=CASCADE)
    payed = models.BooleanField(default=False)

    def __str__(self):
        return "{0}".format(self.name)
