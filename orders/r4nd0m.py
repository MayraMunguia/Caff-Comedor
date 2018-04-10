import sys
sys.path.append(r'C:\Users\Mayra Munguia\Desktop\PyProjects\VentaComedor')
from VentaComedor import settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VentaComedor.settings")
import random
import time
from django.db import connection
import json
from math import *
#from cart.cart import Cart
#from Comedor.models import Product
#from django.test import RequestFactory

#request = None
	
start = time.clock()
count = 138
while (time.clock() - start) < 1200:

	
	cursor = connection.cursor()
	query = cursor.execute('insert into orders_order (created, updated, paid,'+
			' nombre, numeroempleado, numerotarjeta, totalcompra, nomina, razon_social)'+
			'values (now(), now(), 0, "invitado", "-", "-",42, "-", "-");')

	connection.commit()
	que = 'insert into orders_orderitem(price,quantity,order_id,product_id) values (42.00,1,'+ str(count)+',20);'
	print(que)
	query2 = cursor.execute(que)
	connection.commit()
	print('funciona')
	cursor.close()
	
	#enviar un response a ventanaordenes/templates	



	#request_factory = RequestFactory()
	#request = request_factory.get('/',)
	#cart=  Cart(request)


	#for i in range(1,random.randint(1,2)):
	#	product = Product.objects.order_by('?').first()
	#	cart.add(product= product , quantity= random.randint(1,10), update_quantity= False)

	#for item in cart:
	#	OrderItem.objects.create(order=order,product= item['product'], price = item['price'],
	#	 	quantity=item['quantity'])
	#cart.clear()
	count +=1 
	print(count)
	time.sleep(random.randint(1, 20))

