from django import forms
from .models import Carta

class CartaForm(forms.ModelForm):

    class Meta:
        model = Carta
        fields = ['nome', 'imagem']