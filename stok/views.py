from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import Produto

def cadastrar_produto(request):
    if request.method == "GET":
        return render (request, 'cadastrar_produto.html')
    elif request.method =="POST":
        nome1 = request.POST.get('nome')
        preco1 = request.POST.get('preco')
        validade1 = request.POST.get('validade')
        quantidade1 = request.POST.get('quantidade')

        produto = Produto(
            nome=nome1,
            preco=preco1,
            validade=validade1,
            quantidade=quantidade1,
        )


        produto.save()
        return redirect('/stok/listar_produtos')

def listar_produtos(request):
    produtos = Produto.objects.all()
    preco1 = request.GET.get('preco')
    if preco1:
        produtos = produtos.filter(preco__gte=preco1)
    
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect ('/stok/listar_produtos/')