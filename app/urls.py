from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index' ),
    path('dados_graficos',views.dados_graficos, name='dados_graficos'),
]