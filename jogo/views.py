import random

from django.shortcuts import render, redirect, get_object_or_404
from .models import Carta
from .forms import CartaForm


def inicio(request):
    return render(request, 'jogo/inicio.html')


def listar_cartas(request):
    cartas = Carta.objects.all()

    return render(request, 'jogo/listar_cartas.html', {
        'cartas': cartas
    })


def criar_carta(request):
    if request.method == 'POST':
        form = CartaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('listar_cartas')

    else:
        form = CartaForm()

    return render(request, 'jogo/criar_carta.html', {
        'form': form
    })


def excluir_carta(request, id):
    carta = get_object_or_404(Carta, id=id)
    carta.delete()

    return redirect('listar_cartas')


def editar_carta(request, id):
    carta = Carta.objects.get(id=id)

    if request.method == 'POST':
        form = CartaForm(request.POST, request.FILES, instance=carta)

        if form.is_valid():
            form.save()
            return redirect('listar_cartas')

    else:
        form = CartaForm(instance=carta)

    return render(request, 'jogo/editar_carta.html', {
        'form': form
    })


def jogo(request):
    cartas = list(Carta.objects.all())
    cartas = cartas * 2
    random.shuffle(cartas)

    return render(request, 'jogo/jogo.html', {
        'cartas': cartas
    })