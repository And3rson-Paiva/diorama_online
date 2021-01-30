from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth.models import User
from datetime import timedelta


#imagem = StdImageField('Imagem', upload_to='usuarios', variations={'thumb': (124, 124)})
#arq = models.FileField('Arquivos', upload_to='arquivos')


class Empresas(models.Model):
    usuario = models.ForeignKey(User, verbose_name='Sócio', on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=14, verbose_name='CNPJ')
    razao_social = models.CharField(max_length=150, verbose_name='Razão Social')
    nome_fantasia = models.CharField(max_length=150, verbose_name='Nome Fantasia')
    cnae = models.CharField(max_length=7, verbose_name='Cnae')
    logradouro = models.CharField(max_length=200, verbose_name='Logradouro')
    numero = models.IntegerField(verbose_name='Número')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    estado = models.CharField(max_length=100, verbose_name='Estado')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    municipio = models.CharField(max_length=100, verbose_name='Município')
    SIM = 'Sim'
    NAO = 'Não'
    ATIVO = [
        (SIM, 'Sim'),
        (NAO, 'Não'),
    ]
    ativo = models.CharField(
        max_length=3,
        choices=ATIVO,
        default=SIM,
        verbose_name='Ativo',
    )
    atividade = models.CharField(max_length=200, verbose_name='Atividade')
    fone = models.CharField(max_length=16, verbose_name='Telefone')
    complemento = models.CharField(max_length=150, verbose_name='Complemento')
    cep = models.IntegerField(verbose_name='CEP')
    inscricao_estadual = models.CharField(max_length=9, verbose_name='Inscrição Estadual')
    inscricao_municipal = models.CharField(max_length=11, verbose_name='Inscrição Municipal')

    def __str__(self):
        return f'{self.nome_fantasia} {self.cnpj}'


class Arquivos(models.Model):
    empresa = models.ForeignKey(Empresas, verbose_name='Empresa', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, verbose_name='Sócio', on_delete=models.CASCADE)
    titulo = models.CharField(blank=True, max_length=150, verbose_name='Título')
    descricao = models.TextField(null=True, blank=True, verbose_name='Descrição')
    data_envio = models.DateField()
    arquivo = models.FileField(upload_to='arquivos')
    GUIAS = 'Guias'
    BALANCETES = 'Balancetes e Demonstrativos'
    DP = 'Departamento Pessoal'
    LIVROS = 'Livros fiscais e contábeis'
    COBRANCAS = 'Cobranças'
    PROTOCOLOS = 'Protocolos'
    CATEGORIAS = [
        (GUIAS, 'Guias'),
        (BALANCETES, 'Balancetes e Demonstrativos'),
        (DP, 'Departamento Pessoal'),
        (LIVROS, 'Livros fiscais e contábeis'),
        (COBRANCAS, 'Cobranças'),
        (PROTOCOLOS, 'Protocolos'),
    ]
    categorias = models.CharField(
        max_length=100,
        choices=CATEGORIAS,
        default=GUIAS,
    )


    def __str__(self):
        return f'{self.arquivo}'


class Eventos(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    inicio = models.DateField('Início', auto_now=False, auto_now_add=False)
    vencimento = models.DateField('Dia do vencimento', auto_now=False, auto_now_add=False, null=True, blank=True)
    estado = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return f'Evento para {self.empresa} {self.inicio} {self.vencimento}'

    def save(self, *args, **kwargs):
        self.vencimento = self.vencimento
        super().save(*args, **kwargs)
