import uuid

from django.db import models

from stdimage.models import StdImageField


# Gerar nomes aleatórios para fotos de upload
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return filename


class Base(models.Model):

    criado = models.DateField("Criação", auto_now_add=True)
    modificado = models.DateField("Atualização", auto_now=True)
    ativo = models.BooleanField("Ativo", default=True)

    class Meta:
        abstract = True


class Servico(Base):

    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField("Serviço", max_length=100)
    descricao = models.TextField("Descrição", max_length=200)
    icone = models.CharField("Icones", max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.servico


class Cargo(Base):

    cargo = models.CharField("Cargo", max_length=100)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.cargo


class Funcionario(Base):

    nome = models.CharField("Nome", max_length=100)
    cargo = models.ForeignKey(Cargo, verbose_name="Cargo", on_delete=models.CASCADE)
    bio = models.TextField("Bio", max_length=200)
    imagem = StdImageField(
        "Imagem", 
        upload_to=get_file_path, 
        variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}
    )
    facebook = models.CharField("Facebook", max_length=150, default='#')
    instagram = models.CharField("Instagram", max_length=150, default='#')
    twitter = models.CharField("Twitter", max_length=150, default='#')

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return self.nome


class Preco(Base):

    STATUS_CHOICES = (
        ('PRO', 'PRO'),
        ('PLUS', 'PLUS'),
        ('PREMIUM', 'PREMIUM'),
    )
    preco = models.DecimalField("Preço", max_digits=8, decimal_places=2)
    status = models.CharField("Status", max_length=10, choices=STATUS_CHOICES)
    usuario = models.IntegerField("Quantidade Usuários", default=0)
    armazenamento = models.CharField("Armazenamento", max_length=10)
    suporte = models.CharField("Suporte", max_length=30)
    atualizacao = models.CharField("Atualização", max_length=30)

    class Meta:
        verbose_name = "Preço"
        verbose_name_plural = "Preços   "

    def __str__(self):
        return  f"R$ {self.preco}/mês {self.status}"
    
    def formata_preco(self):
        return f"R$ {self.preco:.2f}"
    

class Feature(Base):
    
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-laptop-phone', 'Laptop'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    titulo = models.CharField("Título", max_length=50)
    descricao = models.TextField("Descrição", max_length=100)
    icone = models.CharField("Icone", max_length=17, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"

    def __str__(self):
        return self.titulo


class Cliente(Base):

    nome = models.CharField("Nome", max_length=100)
    profissao = models.CharField("Profissão", max_length=50)
    depoimento = models.TextField("Depoimento", max_length=200)
    imagem = StdImageField(
        "Imagem", 
        upload_to=get_file_path, 
        variations={'thumb': {'width': 75, 'height': 75, 'crop': True}}
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome





