from django import forms
from .models import Productos
from .models import Pedidos


class LaForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)



class ProductosForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Productos

        # specify fields to be used
        fields = [
            "nombre",
            "precio",
            "codigo",
            "categoria",
            "estado",
            "imagen",
        ]

class PedidosForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Pedidos

        # specify fields to be used
        fields = [
            "nombre",
            "telefono",
            "pedido_recibido",
            "fecha",
            "direccion",
            "hora",
            "sabor",
            "porciones",
            "abono",
            "precio",
            "imagen",
        ]


      
