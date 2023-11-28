from django.shortcuts import render, redirect
from .models import Reservas
from .forms import ReservasForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def SobreNosotros(request):
    return render(request, 'SobreNosotros.html')

def ReservasGuardar(request):
    if request.method == 'POST':
        form = ReservasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListaDeReservas')
    else:
        form = ReservasForm()
    return render(request, 'Reservas.html', {'form': form})

def ListaDeReservas(request):
    Lista = Reservas.objects.all()
    return render(request, 'ListaDeReservas.html', {'Lista': Lista})

def BorrarReserva(request, id):
    reserva = Reservas.objects.get(id=id)
    reserva.delete()
    return redirect('ListaDeReservas')

def EditarReserva(request, id):
    reserva = Reservas.objects.get(id=id)
    if request.method == 'POST':
        form = ReservasForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('ListaDeReservas')
    else:
        form = ReservasForm(instance=reserva)
    return render(request, 'EditarReserva.html', {'form': form})