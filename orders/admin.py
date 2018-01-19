from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
	list_display = ['id','numerotarjeta', 'nombre', 'numeroempleado', 'totalcompra']
	list_filter= ['paid', 'created', 'updated', 'numeroempleado']
	inlines = [OrderItemInline]
	

admin.site.register(Order,OrderAdmin)