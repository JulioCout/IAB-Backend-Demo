from django.db import models

class Usuario(models.Model):
    CARGO_LISTA = {

    }
    
    nome = models.CharField(max_length=50)
    email = models.EmailField(blank=False, max_length=30)
    cargo = models.CharField(max_length=30, choices=CARGO_LISTA)
    

    def __str__(self):
        return self.nome



class Membro(models.Model):
    TIPO_ENDERECO = {
        'Residencial': 'Residencial',
        'Comercial': 'Comercial'
    }

    nome = models.CharField(max_length=50)
    matricula = models.IntegerField()
    data_posse= models.DateField()
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    oab = models.CharField(max_length=13)
    estado_civil = models.CharField(max_length=12)
    sexo = models.CharField(max_length=12)
    nascimento = models.DateField()
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    naturalidade = models.CharField(max_length=100)
    area_preferencial = models.CharField(max_length=100)
    especialidade = models.TextField(max_length=100)
    proponente = models. TextField(max_length=100)

    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=40)
    cidade = models.CharField(max_length=40)
    complemento = models.CharField(max_length=50)
    tipo = models.CharField(max_length=100, choices=TIPO_ENDERECO)

    def __str__(self):
        return self.nome
    

class Mandato(models.Model):
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=300)
    portaria = models.CharField(max_length=10)
    posse = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.cargo
    
class Indicacao(models.Model):
    COMISSOES_LIST = {
        'DIVERSIDADE': 'Comissão da Diversidade',
        'ADMISSAO_DE_SOCIOS': 'Comissão de Admissão de Sócios',
        'ASSUNTOS_REGULATORIOS': 'Comissão de Assuntos Regulatórios',
        'COMPLIANCE_GOVERNACA': 'Comissão de Compliance e Governança',
        'CRIMINOLOGIA': 'Comissão de Criminologia',
        'DEFESA_DEFICIENCIA': 'Comissão de Defesa das Pessoas com Deficiência',
        'ADUANEIRO_MARITIMO_PORTUARIO': 'Comissão de Direito Aduaneiro, Marítimo e Portuário',
        'TRABALHO_SINDICAL': 'Comissão do Direito Coletivo do Trabalho e Direito Sindical',
        'COOPERATIVO': 'Comissão de Direito Cooperativo',
        'INFRAESTRUTURA': 'Comissão de Direito da Infraestrutura',
        'DESPORTIVO': 'Comissão de Direito Desportivo',
        'TERCEIRO_SETOR': 'Comissão de Direito do Terceiro Setor',
        'TRANSITO_MOBILIDADE': 'Comissão de Direito do Trânsito e Mobilidade Urbana',
        'LIBERDADE_RELIGIOSA': 'Comissão de Direito da Liberdade Religiosa',
        'POLITICAS_PUBLICAS': 'Comissão de Direito e Políticas Públicas',
        'ELEITORAL': 'Comissão de Direito Eleitoral',
        'MEDICO_SAUDE_BIOETICA': 'Comissão de Direito Médico, Sáude e Bioética',
        'PROCESSUAL_CIVIL': 'Comissão de Direito Processual Civil',
        'URBANISTICO': 'Comissão de Direito Urbanístico',
        'RELACOES_UNIVERSITARIAS': 'Comissão de Educação e Relações Universitárias',
        'ENERGIA_TRANSICAO': 'Comissão de Energia e Transição Energética',
        '1950_ATE_HOJE': 'Comissão de Estudos Brasileiros de 1950 até os dias de hoje',
        'IGUALDADE_RACIAL': 'Comissão de Igualdade Racial',
        'MEDIACAO_CONCILIACAO': 'Comissão de Mediação, Conciliação e Arbitragem',
        'PROPRIEDADE_INDUSTRIAL': 'Comissão de Propriedade Industrial',
        'SANEAMENTO_HIDRICOS': 'Comissão de Saneamento e Recursos Hídricos',
        'SEGURIDADE_SOCIAL': 'Comissão de Seguridade Social',
        'ADMINISTRATIVO': 'Comissão de Direito Administrativo',
        'AGRARIO': 'Comissão de Direito Agrario',
        'AMBIENTAL': 'Comissão de Direito Ambiental',
        'AUTORAL': 'Comissão de Direito Autoral',
        'CIVIL': 'Comissão de Direito Civil',
        'CONSTITUCIONAL': 'Comissão de Direito Constitucional',
        'CONSUMIDOR': 'Comissão de Direito do Consumidor',
        'DIGITAL': 'Comissão de Direito Digital',
        'EMPRESARIAL': 'Comissão de Direito Empresarial',
        'FAMILIA_SUCESSAO': 'Comissão de Direito da Familia e Sucessões',
        'FINANCEIRO_TRIBUTARIO': 'Comissão de Direito Financeiro e Tributário',
        'IMOBILIARIO': 'Comissão de Direito Imobiliário',
        'INTEGRACAO': 'Comissão de Direito de Integração',
        'INTERNACIONAL': 'Comissão de Direito Internacional',
        'PENAL': 'Comissão de Direito Penal',
        'TRABALHO': 'Comissão de Direito do Trabalho',
        'HUMANOS': 'Comissão de Direitos Humanos',
        'MULHER': 'Comissão dos Direitos da Mulher',
        'IA_INOVACAO': 'Comissão Especial de Inteligência Artificial e Inovação',
        'FILOSOFIA': 'Comissão Filosofia do Direito',
        '180_ANOS': 'Comissão Temporária de 180 anos',
        '2030_SUSTENTAVEL': 'Comissão Temporária de estudos sobre a agenda 2030 para o desenvolvimento sustentável/ONU',
        'AUGUSTO_FREITAS': 'Comissão Temporária sobre Augusto Teixeira de Freitas'
    }

    STATUS_LIST = {
        'AD_REFEREDUM':'Ad Referendum',
        'AG_NOVO_AGENDAMENTO': 'Aguardando novo agendamento',
        'AGENDADO_PARA_SESSAO_ORDINARIA': 'Agendado para Sessão Ordinária',
        'APENSADA_A_INDICACAO_N032024': 'Apensada à indicação nº 03/2024',
        'APENSADA_A_INDICACAO_N442023': 'Apensada à indicação nº 44/2023',
        'APROVADO': 'Aprovado',
        'APROVADO_MAIORIA': 'Aprovado pela maioria',
        'APROVADO_COMISSAO_AGUARD_PLENARIO': 'Aprovado na Comissão - Aguardando pauta em plenário',
        'APROVADO_PARCIALMENTE': 'Aprovado parcialmente',
        'APROVADO_UNANIMAMENTE': 'Aprovado unanimamente',
        'ARQUIVADO': 'Arquivado',
        'ATIVO': 'Ativo',
        'ENTREGUE_POR_UMA_COMISSAO': 'Entregue por uma comissão - Aguardando as demais',
        'NA_COMISSAO_PARA_ ELABORACAO_DE_PARECER': 'Nas Comissões para elaboração de parecer',
        'PARECER_ENTREGUE_AG_VOTACAO': 'Parecer entregue - Aguardando votação na Comissão',
        'PERDA_DE_OBJETO': 'Perda de Objeto',
        'REJEITADO': 'Rejeitado',
        'REJEITDO_MAIORIA': 'Rejeitado pela maioria',
        'REJEITADO_UNANIMAMENTE': 'Rejeitado Unanimamente',
        'SOBRESTADO': 'Sobrestado'
    }

    MOV_TIPO_LIST = {
        'CONCLUSAO_PARECER': 'Conclusão do Parecer',
        'DECISAO_PLENARIO': 'Decisão do Plenário',
        'PARECER': 'Parecer',
        'PAUTA': 'Pauta',
        'RECEBIMENTO': 'Recebimento',
        'REMESSA': 'REMESSA'
    }
    
    numero = models.CharField(max_length=10)
    autor = models.ForeignKey(Membro, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_LIST)
    cadastro = models.DateField()
    projeto_lei = models.CharField(max_length=100)
    objeto = models.TextField()
    materia = models.TextField()
    comissoes = models.CharField(max_length=100)
    relator = models.TextField()
    tag = models.CharField(max_length=500)

    mov_data = models.DateField(null=True, blank=True)
    mov_tipo = models.CharField(max_length=30, choices=MOV_TIPO_LIST, null=True)
    mov_descricao = models.TextField(null=True, blank=True)
    mov_data_agenda = models.DateField(null=True, blank=True)
    mov_avisar_email = models.BooleanField(default=True)

    def __str__(self):
        return self.numero

class Movimentacao(models.Model):
    indicacao = models.ForeignKey(Indicacao, on_delete=models.CASCADE)
    data = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    agenda = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Processo(models.Model):
    numero_justica = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    tribunal = models.CharField(max_length=100)
    comarca = models.CharField(max_length=100)
    camara_turma = models.CharField(max_length=100)
    fase_atual = models.CharField(max_length=100)
    data_fase = models.DateField()
    relator_tribunal = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    observacoes = models.TextField(max_length=100)
