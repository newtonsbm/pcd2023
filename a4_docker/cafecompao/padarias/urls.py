from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('minha-conta', views.minha_conta, name='minha_conta'),
    path('sugestao', views.sugestao, name='sugestao'),
    # PADARIAS
    path('padarias/listar', views.PadariaListView.as_view() , name='padarias_list'),
    path('padarias/<int:pk>', views.PadariaDetailView.as_view() , name='padarias_detail'),
    # CESTAS 
    path('cestas/listar', views.CestaListView.as_view() , name='cestas_list'),
    path('cestas/<pk>', views.CestaDetailView.as_view() , name='cestas_detail'),
    # ASSINATURAS 
    path('assinaturas/criar', views.AssinaturaCreateView.as_view(), name='assinaturas_create'),
    path('assinaturas/editar/<pk>', views.AssinaturaUpdateView.as_view(), name='assinaturas_update'),
    path('assinaturas/cancelar/<pk>', views.AssinaturaDeleteView.as_view(), name='assinaturas_delete'),
]

