# Generated by Django 3.1.3 on 2020-12-20 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('razao_social', models.CharField(max_length=150, verbose_name='Razão Social')),
                ('nome_fantasia', models.CharField(max_length=150, verbose_name='Nome Fantasia')),
                ('cnae', models.CharField(max_length=7, verbose_name='Cnae')),
                ('logradouro', models.CharField(max_length=200, verbose_name='Logradouro')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('municipio', models.CharField(max_length=100, verbose_name='Município')),
                ('ativo', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Sim', max_length=3, verbose_name='Ativo')),
                ('atividade', models.CharField(max_length=200, verbose_name='Atividade')),
                ('fone', models.CharField(max_length=16, verbose_name='Telefone')),
                ('complemento', models.CharField(max_length=150, verbose_name='Complemento')),
                ('cep', models.IntegerField(verbose_name='CEP')),
                ('inscricao_estadual', models.CharField(max_length=9, verbose_name='Inscrição Estadual')),
                ('inscricao_municipal', models.CharField(max_length=11, verbose_name='Inscrição Municipal')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Sócio')),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField(auto_now_add=True, verbose_name='Início')),
                ('vencimento', models.DateField(blank=True, null=True, verbose_name='Dia do vencimento')),
                ('estado', models.BooleanField(default=True, verbose_name='Ativo')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.empresas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='Arquivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=150, verbose_name='Título')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('data_envio', models.DateField()),
                ('arquivo', models.FileField(upload_to='arquivos')),
                ('categorias', models.CharField(choices=[('Guias', 'Guias'), ('Balancetes e Demonstrativos', 'Balancetes e Demonstrativos'), ('Departamento Pessoal', 'Departamento Pessoal'), ('Livros fiscais e contábeis', 'Livros fiscais e contábeis'), ('Cobranças', 'Cobranças'), ('Protocolos', 'Protocolos')], default='Guias', max_length=100)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.empresas', verbose_name='Empresa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Sócio')),
            ],
        ),
    ]
