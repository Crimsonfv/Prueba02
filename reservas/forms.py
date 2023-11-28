from django import forms
from .models import Reservas
from django.core import validators


estados = [
    ('RESERVADO', 'RESERVADO'),
    ('COMPLETADA', 'COMPLETADA'),
    ('ANULADA', 'ANULADA'),
    ('NO ASISTEN', 'NO ASISTEN'),
]

class ReservasForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre', max_length=80, required=True, widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'Ingrese solo letras',"class":"form-control"}))
    telefono = forms.CharField(label='Telefono', max_length=50, required=True, widget=forms.TextInput(attrs={'pattern': '[0-9+]+', 'title': 'Ingrese solo números',"class":"form-control"}),)
    fechayHoraDeReserva = forms.DateTimeField(label='Fecha y Hora de Reserva', required=True, input_formats=['%Y-%m-%d %H:%M'],widget=forms.DateTimeInput(attrs={'placeholder': '2022-12-22 18:00', "class":"form-control", "type":"datetime"}),error_messages={'invalid': 'Por favor, introduce una fecha y hora válidas. Por ejemplo: 2022-12-14 18:00.',})
    cantidadDePersonas = forms.IntegerField(label='Cantidad de Personas', required=True,validators=[ validators.MinValueValidator(1, message = "Minimo debe ser una persona"), validators.MaxValueValidator(15, message = "Maximo 15 personas")],widget=forms.NumberInput(attrs={"class":"form-control"}) )
    correo = forms.EmailField(label='Correo', required=True, error_messages={'invalid': 'Introduce un correo valido debe tener @ y . Ejemplo: Guillermo@gmail.com'}, widget=forms.EmailInput(attrs={"class":"form-control"}) )
    estado = forms.ChoiceField(label='Estado', required=True, choices=estados, widget=forms.Select(attrs={"class":"form-control"}) )
    observaciones = forms.CharField(label='Observaciones', required=False,widget=forms.Textarea(attrs={"class":"form-control", "rows":"4"}))

    class Meta:
        model = Reservas
        fields = ['nombre', 'telefono', 'fechayHoraDeReserva', 'cantidadDePersonas', 'correo', 'estado', 'observaciones']