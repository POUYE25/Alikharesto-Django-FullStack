from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from dishes.models import Dish
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from datetime import date

def clean(self):
    if self.date < date.today():
        raise ValidationError("La date de réservation ne peut pas être dans le passé.")


User = get_user_model()

class Table(models.Model):
    number       = models.PositiveSmallIntegerField(unique=True)
    seats        = models.PositiveSmallIntegerField("Places")
    is_available = models.BooleanField("Libre", default=True)

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"Table {self.number} – {self.seats}p ({'libre' if self.is_available else 'occupée'})"


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'En attente'),
        ('CONFIRMED', 'Confirmée'),
        ('CANCELLED', 'Annulée'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='reservations')
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('table', 'date', 'time')

    def __str__(self):
        return f"Réservation #{self.id} – Table {self.table.number} le {self.date} à {self.time}"


class Menu(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=7, decimal_places=2)
    dishes      = models.ManyToManyField(Dish, related_name="menus", blank=True)

    def __str__(self):
        return f"{self.name} ({self.price} €)"

class Order(models.Model):
    PENDING, IN_PROGRESS, DONE, CANCELED = "P","I","D","C"
    STATUS_CHOICES = [
        (PENDING,    "En attente"),
        (IN_PROGRESS,"En cours"),
        (DONE,       "Terminée"),
        (CANCELED,   "Annulée"),
    ]

    customer   = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    table      = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    menus      = models.ManyToManyField(Menu, blank=True, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    status     = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)

    def total_amount(self):
        return sum(m.price for m in self.menus.all())

    def __str__(self):
        return f"Commande #{self.pk} – {self.get_status_display()}"

class Payment(models.Model):
    CASH, CARD, ONLINE = "cash", "card", "online"
    METHOD_CHOICES = [
        (CASH,   "Espèces"),
        (CARD,   "Carte"),
        (ONLINE, "En ligne"),
    ]

    order     = models.OneToOneField(Order, related_name="payment", on_delete=models.CASCADE)
    amount    = models.DecimalField(max_digits=8, decimal_places=2)
    method    = models.CharField(max_length=10, choices=METHOD_CHOICES)
    confirmed = models.BooleanField(default=False)
    paid_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Paiement {self.amount} € ({self.get_method_display()})"



