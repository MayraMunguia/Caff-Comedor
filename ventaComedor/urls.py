from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^ventanaOrdenes/', include('ventanaOrdenes.urls', namespace='ventanaOrdenes')),
    url(r'^reportes/', include('reportes.urls', namespace='reportes')),
    url(r'^', include('comedor.urls', namespace='ventaComedor')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)