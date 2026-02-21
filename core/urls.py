from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('tables/', views.table_list, name='table_list'),
    path('menus/', views.menu_list, name='menu_list'),

    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.order_add, name='order_add'),

    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/new/', views.reservation_new, name='reservation_new'),

    path('payments/', views.payment_list, name='payment_list'),
    path('payment/add/', views.payment_add, name='payment_add'),
]