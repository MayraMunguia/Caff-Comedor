from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['numerotarjeta']

class OrderCashForm(forms.Form):
	Pago= forms.IntegerField(min_value=0)
		
