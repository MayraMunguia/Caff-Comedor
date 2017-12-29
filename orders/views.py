from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm, OrderCashForm
from cart.cart import Cart
import MySQLdb
from django.contrib import messages

	
def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		form2 = OrderCashForm(request.POST)
		if form2.is_valid():
			data = form2.cleaned_data
			
			pago = data['Pago']
			total = cart.get_total_price()
			cambio = pago - total 
			
			order = form.save()
			for item in cart:
				OrderItem.objects.create(order=order,product= item['product'], price = item['price'], quantity=item['quantity'])
			cart.clear()
			
			return render(request, 'orders/order/createdEfectivo.html', {'order':order, 'cambio': cambio})
		elif form.is_valid():
			data = form.cleaned_data	
			numerotarjeta = data['numerotarjeta']
		
			db = MySQLdb.connect(user='root', db='test', passwd='t38l7b+a', host='localhost')
			cursor = db.cursor()
			query = cursor.execute('SELECT * FROM empleados WHERE numerotarjeta = "%s"' % numerotarjeta)
			if query > 0 :
				nombres = cursor.fetchall()
				db.close()	

				order = form.save(commit = False)
				order.nombre = str(nombres[0][0])
				order.numeroempleado= str(nombres[0][1])  
				order =  form.save()
				nom = str(nombres[0][0]) 
				total = cart.get_total_price()
				for item in cart:
					OrderItem.objects.create(order=order,product= item['product'], price = item['price'], quantity=item['quantity'])
				cart.clear()
				return render(request, 'orders/order/createdTarjeta.html', {'nombre':nom, 'total':total})			
			else:	
				db.close()
				messages.info(request, '! Tu numero de tarjeta no se encuentra en la base de datos, porfavor intenta denuevo.')	
				return render(request, 'orders/order/payment.html')

		else:
			return render(request,'orders/order/payment.html')


	elif 'Tarjeta' in request.GET: 
		form = OrderCreateForm()
		return render(request, 'orders/order/ordentarjeta.html',{'cart':cart, 'form':form})
	else: 
		form = OrderCashForm()
		return render(request, 'orders/order/ordenefectivo.html',{'cart':cart, 'form':form})
		

def clear_session(request):
	cart = Cart(request)
	cart.clear()

	return redirect('/')

def payment(request):
	return render(request,'orders/order/payment.html')
	
