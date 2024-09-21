from financeiroData.models import Despesa, Receita
from financeiroData.serializers import DespesaSerializer, ReceitaSerializer
from rest_framework import viewsets

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer