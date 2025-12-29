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
        ano_fabricacao1 = request.POST.get('ano_fabricacao')
        preco1 = Decimal(request.POST.get('preco').replace('.', '').replace(',', '.'))
        tipo1 = request.POST.get('tipo')
        estado1 = request.POST.get('estado')
        cor1 = request.POST.get('cor')
        foto1 = request.FILES.get('foto')

        produto = Produto(
            marca=marca1,
            modelo=modelo1,
            ano_fabricacao=ano_fabricacao1,
            preco=preco1,
            tipo=tipo1,
            estado=estado1,
            cor=cor1,
            foto=foto1,
        )


        produto.save()
        return redirect('/stok/listar_produtos')

def listar_produtos(request):
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