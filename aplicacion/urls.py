from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('paginaes/', views.estudiante,name='estudiante'),
    path('paginages/', views.gestionar,name='gestionar'),
    path('paginaho/', views.horarios,name='horarios'),
    path('paginapo/', views.portafolio,name='portafolio'),
    path('paginaFor1/', views.form_pro,name='form_pro'),
    path('paginaedi/<id_profe>/', views.modificar,name='modificar'),
    path('paginaelim/<id_profe>', views.eliminar, name='eliminar'),
]