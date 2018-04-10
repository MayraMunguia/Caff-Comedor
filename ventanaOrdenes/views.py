from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.template import RequestContext,loader
from django.http import JsonResponse
import json


def servicio(request):
	cursor = connection.cursor()
	query = cursor.execute('select b.nombre, b.totalcompra, a.order_id, c.name, a.quantity'+
	' FROM orders_order b JOIN orders_orderitem a JOIN comedor_product c '+
	'WHERE a.product_id = c.id AND b.id = a.order_id AND (TIMESTAMPDIFF(SECOND, b.created, now()) <= 60)'+
	' ORDER BY b.created DESC LIMIT 8;')
	ordenes = cursor.fetchall()
	return HttpResponse(loader.get_template('servicio.html').render(RequestContext(request,{'ordenes': ordenes})))


def update(request):
	cursor = connection.cursor()
	query = cursor.execute('SELECT b.nombre, b.totalcompra, a.order_id,'+
		'CONCAT(C.name, " x " ,a.quantity) AS productos '+
		'FROM orders_order b JOIN orders_orderitem a JOIN comedor_product c '+
		'WHERE a.product_id = c.id AND b.id = a.order_id '+
		'  ORDER BY b.created DESC LIMIT 8;')
	ordenes = cursor.fetchall()
	keys = ('nombre','total', 'orden', 'producto',)
	result = []
	for orden in ordenes:
		result.append(dict(zip(keys,orden)))
	i = 0
	while i < (len(result) - 1):
		if result[i].get('orden') == result[i + 1].get('orden'):
			result[i].update({'producto': result[i].get('producto') +  '<br>' + result[i + 1].get('producto')}) 
			del result[i+1]
		i += 1
	jdt = json.dumps(result)	
	jdata= json.loads(jdt)
	return JsonResponse(jdata, safe=False)