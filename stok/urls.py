from django.urls import path
from . import views

urlpatterns = [

    path('cadastrar_produto/', views.cadastrar_produto, name="cadastrar_produto"),
    path('listar_produtos/', views.listar_produtos, name="listar_produtos_preco"),
    path('deletar_produto/<int:id>/', views.deletar_produto)
]