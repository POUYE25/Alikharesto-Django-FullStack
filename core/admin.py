from django.contrib import admin
from .models import Table, Menu, Order, Payment
from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('table', 'date', 'time', 'user', 'status')
    list_filter = ('date', 'status')
    search_fields = ('user__username', 'table__number')
    # Permet à l'admin de choisir l'utilisateur dans une liste de recherche
    raw_id_fields = ('user',)
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display  = ("number", "seats", "is_available")
    list_editable = ("is_available",)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    filter_horizontal = ("dishes",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "table", "created_at", "status", "total_amount")
    list_filter  = ("status",)
    date_hierarchy = "created_at"

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "amount", "method", "confirmed", "paid_at")
    list_filter  = ("method", "confirmed")