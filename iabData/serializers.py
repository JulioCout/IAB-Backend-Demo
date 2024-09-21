from rest_framework import serializers
from iabData.models import Membro, Mandato, Indicacao, Movimentacao, Processo

class MembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membro
        fields = '__all__'

class MandatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mandato
        fields = '__all__'

class IndicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicacao
        fields = '__all__'

class MovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = '__all__'

class ProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processo
        fields = '__all__'