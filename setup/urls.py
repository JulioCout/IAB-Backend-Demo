from django.contrib import admin
from django.urls import path, include
from iabData.views import MembroViewSet, MandatoViewSet, IndicacaoViewSet, MovimentacaoViewSet, ProcessoViewSet
from financeiroData.views import DespesaViewSet, ReceitaViewSet

from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('membros', MembroViewSet, basename='Membros')
router.register('mandatos', MandatoViewSet, basename='Mandatos')
router.register('indicacoes', IndicacaoViewSet, basename='Indicações')
router.register('movimentacoes', MovimentacaoViewSet, basename='Movimentacoes')
router.register('processos', ProcessoViewSet, basename='Processos')

router.register('despesas', DespesaViewSet, basename='Despesas')
router.register('receitas', ReceitaViewSet, basename='Receitas')

schema_view = get_schema_view(
   openapi.Info(
      title="API IAB DataBoard",
      default_version='v1',
      description="API para gerenciamento dos dados do Instituto dos Advogados Brasileiros",
      terms_of_service="@",
      contact=openapi.Contact(email="juliocscoutinho@outlook.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
