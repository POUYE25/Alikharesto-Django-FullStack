from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
@receiver(post_save, sender=Order)
def update_table_status(sender, instance, **kwargs):
    if instance.table:
        # La table est libre si la commande est Terminée (DONE) ou Annulée (CANCELED)
        instance.table.is_available = (instance.status in [Order.DONE, Order.CANCELED])
        instance.table.save()
