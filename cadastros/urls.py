from django.urls import path
from .views import NotaCreate, ProventosCreate
from .views import NotaUpdate
from .views import NotaDelete
from .views import NotaList, dash, ProventosList

urlpatterns = [
    #path('endereco', MinhaView.as_view(), name='nome-da-url')
    path('cadastros/nota/', NotaCreate.as_view(), name='cadastrar-nota'),    
    path('cadastros/proventos/', ProventosCreate.as_view(), name='cadastrar-proventos'),

    path('editar/nota/<int:pk>/', NotaUpdate.as_view(), name='editar-nota'),
    
    path('excluir/nota/<int:pk>/', NotaDelete.as_view(), name='excluir-nota'),
    
    path('cadastro/listas/ordens/', NotaList.as_view(), name='listar-ordens'),
    path('cadastro/listas/dashboard/', dash, name='dashboard'),
    path('cadastro/listas/proventos/', ProventosList.as_view(), name='listar-proventos'),
]