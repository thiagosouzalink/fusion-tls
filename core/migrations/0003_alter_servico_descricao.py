# Generated by Django 3.2 on 2021-05-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_funcionario_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='descricao',
            field=models.TextField(max_length=200, verbose_name='Descrição'),
        ),
    ]
