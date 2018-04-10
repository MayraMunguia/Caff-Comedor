from django.db import models
from comedor.models import Product
from datetime import datetime


class Order(models.Model):
	nombre= models.CharField(max_length=100, null=True, blank= True, default='Invitado')
	numerotarjeta= models.CharField(max_length=20, null=True, blank = True)
	numeroempleado= models.CharField(max_length=20, null=True, blank = True, default='-')
	nomina= models.CharField(max_length=50, null=True, blank = True, default='-')
	razon_social= models.CharField(max_length=50, null=True, blank = True, default='-')
	sucursal = models.CharField(max_length=50, null=True, blank = True, default='-')
	area= models.CharField(max_length=50, null=True, blank = True, default='-')
	segmento= models.CharField(max_length=50, null=True, blank = True, default='-')
	correo= models.CharField(max_length=50, null=True, blank = True, default='-')
	created = models.DateTimeField(default= datetime.now)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)
	totalcompra = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
	order = models.ForeignKey(Order,related_name='items')
	product = models.ForeignKey(Product, related_name= 'order_items')
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):	
		return self.price * self.quantity


