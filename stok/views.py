from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import Produto
from decimal import Decimal

def cadastrar_produto(request):
    if request.method == "GET":
        return render (request, 'cadastrar_produto.html')
    
    elif request.method =="POST":
        marca1 = request.POST.get('marca')
        modelo1 = request.POST.get('modelo')
        # --- AJUSTE PARA O CALENDÁRIO ---
        data_full = request.POST.get('ano_fabricacao') # Recebe "2024-05-15"
        if data_full:
            ano_fabricacao1 = data_full.split('-')[0] # Pega apenas "2024"
        else:
            ano_fabricacao1 = None
        km_raw = request.POST.get('quilometragem')
        km_limpo = km_raw.replace('.', '') if km_raw else 0

        # --- AJUSTE PARA O PREÇO COM MÁSCARA ---
        preco_raw = request.POST.get('preco')
        if preco_raw:
            # Transforma "1.500,50" em "1500.50" para o Decimal aceitar
            preco1 = Decimal(preco_raw.replace('.', '').replace(',', '.'))
        else:
            preco1 = Decimal('0.00')

        tipo1 = request.POST.get('tipo')
        estado1 = request.POST.get('estado')
        cor1 = request.POST.get('cor')
        

        produto = Produto(
            marca=marca1,
            modelo=modelo1,
            ano_fabricacao=ano_fabricacao1,
            quilometragem=km_limpo,
            preco=preco1,
            tipo=tipo1,
            estado=estado1,
            cor=cor1,
            
        )

        produto.save()
        return redirect('/stok/listar_produtos')

def listar_produtos(request):
    #lógica dos meus filtros de busca
    produtos = Produto.objects.all()
    preco1 = request.GET.get('preco')
    tipo1 = request.GET.get('tipo')
    if preco1:
        preco_decimal = Decimal(preco1.replace('.', '').replace(',', '.')) 
        produtos = produtos.filter(preco__gte=preco_decimal) # preco__gte - greater than or equal to
    if tipo1:
        produtos = produtos.filter(tipo=tipo1)
    
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect ('/stok/listar_produtos/')