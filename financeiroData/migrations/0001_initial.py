# Generated by Django 5.1 on 2024-09-21 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('data_lançamento', models.DateField(auto_now=True)),
                ('data_efetivacao', models.DateField()),
                ('categoria', models.CharField(max_length=50)),
                ('conta', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('data_lançamento', models.DateField(auto_now=True)),
                ('data_efetivacao', models.DateField()),
                ('categoria', models.CharField(max_length=50)),
                ('conta', models.CharField(max_length=50)),
            ],
        ),
    ]
