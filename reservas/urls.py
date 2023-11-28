from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('SobreNosotros/',views.SobreNosotros, name='SobreNosotros'),	
    path('Reservas/',views.ReservasGuardar, name='Reservas'),
    path('ListaDeReservas/',views.ListaDeReservas, name='ListaDeReservas'),
    path('BorrarReserva/<int:id>/',views.BorrarReserva, name='BorrarReserva'),
    path('EditarReserva/<int:id>/', views.EditarReserva, name='EditarReserva'),
]