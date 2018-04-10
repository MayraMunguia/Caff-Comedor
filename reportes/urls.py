from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.loginRep, name='login'),
	url(r'^cerrar/$', views.cerrar),
	url(r'^consumo/$', views.Reportes,name='reportes'), 
	url(r'^comedor/$', views.reportecomedor,name='reportecomedor'),
	url(r'^empleados/Search/$', views.buscaempleado,name='buscaempleado'),
	url(r'^reporte_empleado/$',views.ReporteEmpleado, name="reporte_empleado"), #para reportes de comidas
	url(r'^reporte_total_excel/$',views.ReporteTotalExcel, name="reporte_total_excel"),
	url(r'^reporte_total_comedor/$',views.ReporteTotalComedor, name="reporte_total_comedor"),

]