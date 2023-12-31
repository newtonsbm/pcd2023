# Generated by Django 4.1.5 on 2023-01-16 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('padarias', '0005_cesta_nivel'),
    ]

    operations = [
        migrations.AddField(
            model_name='padaria',
            name='cestas',
            field=models.ManyToManyField(help_text='Cestas da padaria', related_name='padarias', to='padarias.cesta', verbose_name='Cestas'),
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(help_text='Rua do endereço', max_length=100, verbose_name='Rua')),
                ('numero', models.CharField(help_text='Número do endereço', max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, help_text='Complemento do endereço', max_length=100, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, help_text='Bairro do endereço', max_length=100, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(help_text='Cidade do endereço', max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(help_text='Estado do endereço', max_length=2, verbose_name='Estado')),
                ('cep', models.CharField(help_text='CEP do endereço', max_length=8, verbose_name='CEP')),
                ('padaria', models.OneToOneField(help_text='Padaria do endereço', on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='padarias.padaria', verbose_name='Padaria')),
            ],
        ),
    ]
