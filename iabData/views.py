from iabData.models import Membro, Mandato, Indicacao, Movimentacao, Processo
from iabData.serializers import MembroSerializer, ProcessoSerializer, MovimentacaoSerializer, IndicacaoSerializer, MandatoSerializer
from rest_framework import viewsets

class MembroViewSet(viewsets.ModelViewSet):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer

class MandatoViewSet(viewsets.ModelViewSet):
    queryset = Mandato.objects.all()
    serializer_class = MandatoSerializer

class IndicacaoViewSet(viewsets.ModelViewSet):
    queryset = Indicacao.objects.all()
    serializer_class = IndicacaoSerializer

class MovimentacaoViewSet(viewsets.ModelViewSet):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer

class ProcessoViewSet(viewsets.ModelViewSet):
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer