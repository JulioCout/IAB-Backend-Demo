# Generated by Django 5.1 on 2024-09-03 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('matricula', models.IntegerField()),
                ('data_posse', models.DateField()),
                ('email', models.EmailField(max_length=30)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('oab', models.CharField(max_length=13)),
                ('estado_civil', models.CharField(max_length=12)),
                ('sexo', models.CharField(max_length=12)),
                ('nascimento', models.DateField()),
                ('pai', models.CharField(max_length=100)),
                ('mae', models.CharField(max_length=100)),
                ('nacionalidade', models.CharField(max_length=100)),
                ('naturalidade', models.CharField(max_length=100)),
                ('area_preferencial', models.CharField(max_length=100)),
                ('especialidade', models.TextField(max_length=100)),
                ('proponente', models.TextField(max_length=100)),
                ('cep', models.CharField(max_length=10)),
                ('endereco', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=40)),
                ('cidade', models.CharField(max_length=40)),
                ('complemento', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('Residencial', 'Residencial'), ('Comercial', 'Comercial')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_justica', models.CharField(max_length=100)),
                ('classe', models.CharField(max_length=100)),
                ('tribunal', models.CharField(max_length=100)),
                ('comarca', models.CharField(max_length=100)),
                ('camara_turma', models.CharField(max_length=100)),
                ('fase_atual', models.CharField(max_length=100)),
                ('data_fase', models.DateField()),
                ('relator_tribunal', models.CharField(max_length=100)),
                ('motivo', models.CharField(max_length=100)),
                ('observacoes', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('cargo', models.CharField(choices=[], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mandato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=300)),
                ('portaria', models.CharField(max_length=10)),
                ('posse', models.DateField()),
                ('membro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iabData.membro')),
            ],
        ),
        migrations.CreateModel(
            name='Indicacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('cadastro', models.DateField()),
                ('projeto_lei', models.CharField(max_length=100)),
                ('objeto', models.CharField(max_length=100)),
                ('materia', models.CharField(max_length=100)),
                ('comissoes', models.CharField(max_length=100)),
                ('relator', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iabData.membro')),
            ],
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('tipo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('agenda', models.CharField(max_length=100)),
                ('indicacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iabData.indicacao')),
            ],
        ),
    ]
