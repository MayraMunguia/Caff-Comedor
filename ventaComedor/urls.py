from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import report_builder.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^ventanaordenes/', include('ventanaordenes.urls', namespace='ventanaordenes')),
    url(r'^reportes/', include('reportes.urls', namespace='reportes')),
    url(r'^', include('Comedor.urls', namespace='VentaComedor')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)