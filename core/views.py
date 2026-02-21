from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from .models import Table, Menu, Order, Payment, Reservation
from .forms import PaymentForm, ReservationForm

@login_required(login_url='accounts:login')
def table_list(request):
    tables = Table.objects.all().order_by('number')
    return render(request, 'core/table_list.html', {'tables': tables, 'title': 'Nos tables'})

@login_required(login_url='accounts:login')
def menu_list(request):
    menus = Menu.objects.all().order_by('name')
    return render(request, 'core/menu_list.html', {'menus': menus, 'title': 'Nos menus'})

@login_required(login_url='accounts:login')
def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'core/order_list.html', {'orders': orders, 'title': 'Commandes'})

@login_required(login_url='accounts:login')
def order_add(request):
    # Logique simplifiée pour ajouter une commande
    return render(request, 'core/order_form.html', {'title': 'Passer une commande'})

@login_required(login_url='accounts:login')
def reservation_new(request):
    """ Création de réservation associée à l'utilisateur connecté """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user 
            reservation.save()
            return redirect('core:reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'core/reservation_form.html', {'form': form, 'title': 'Réserver une table'})

@login_required(login_url='accounts:login')
def reservation_list(request):
    """ L'utilisateur ne voit que SES réservations """
    reservations = Reservation.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'core/reservation_list.html', {'reservations': reservations, 'title': 'Mes réservations'})

@login_required(login_url='accounts:login')
def payment_add(request):
    """ Traitement du paiement d'une commande """
    order_id = request.GET.get('order_id')
    initial = {}

    if order_id:
        order = get_object_or_404(Order, pk=order_id)
        initial = {'order': order, 'amount': order.total_amount()}

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.confirmed = True 
            payment.save()

            # Mise à jour du statut de la commande
            if payment.order:
                payment.order.status = Order.DONE
                payment.order.save()
            return redirect('core:payment_list')
    else:
        form = PaymentForm(initial=initial)

    return render(request, 'core/payment_form.html', {'form': form, 'title': 'Régler la commande'})

@login_required(login_url='accounts:login')
def payment_list(request):
    payments = Payment.objects.all().order_by('-paid_at')
    return render(request, 'core/payment_list.html', {'payments': payments, 'title': 'Historique des paiements'})