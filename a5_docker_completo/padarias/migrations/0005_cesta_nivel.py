# Generated by Django 4.1.5 on 2023-01-16 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padarias', '0004_cesta'),
    ]

    operations = [
        migrations.AddField(
            model_name='cesta',
            name='nivel',
            field=models.CharField(choices=[('B', 'Básico'), ('M', 'Médio'), ('P', 'Premium')], default='B', help_text='Nível da cesta', max_length=1, verbose_name='Nível'),
        ),
    ]
