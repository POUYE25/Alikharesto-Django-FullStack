from django import forms
from .models import Payment
from django import forms
from .models import Reservation

class PaymentForm(forms.ModelForm):
    class Meta:
        model  = Payment
        fields = ['order', 'amount', 'method']



class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'date', 'time', 'party_size']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }