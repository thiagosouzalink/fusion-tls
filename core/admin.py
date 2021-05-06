from django.contrib import admin

from .models import Cargo, Servico, Funcionario, Preco, Feature, Cliente


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):

    list_display = ['cargo', 'modificado', 'ativo']


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):

    list_display = ['servico', 'icone', 'ativo', 'modificado']


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):

    list_display = ['nome', 'cargo', 'modificado', 'ativo']


@admin.register(Preco)
class PrecoAdmin(admin.ModelAdmin):

    list_display = ['formata_preco', 'status', 'armazenamento', 'criado']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'criado']


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    list_display = ['nome', 'profissao', 'criado']
