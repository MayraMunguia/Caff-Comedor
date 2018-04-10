from django import forms
import datetime
from datetime import timedelta
from django.forms.extras.widgets import SelectDateWidget


class RangoFechaForm(forms.Form):
	tomorrow = datetime.date.today() + timedelta(1)
	yesterday = datetime.date.today() - timedelta(1)
	Desde= forms.DateField(widget=SelectDateWidget(), initial=yesterday)
	Hasta= forms.DateField(widget=SelectDateWidget(), initial=tomorrow)
		
