from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jogo.views import inicio, listar_cartas, criar_carta, excluir_carta, editar_carta, jogo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('cartas/', listar_cartas, name='listar_cartas'),
    path('cartas/criar/', criar_carta, name='criar_carta'),
    path('cartas/excluir/<int:id>/', excluir_carta, name='excluir_carta'),
    path('cartas/editar/<int:id>/', editar_carta, name='editar_carta'),
    path('jogo/', jogo, name='jogo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
