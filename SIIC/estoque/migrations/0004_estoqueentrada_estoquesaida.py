# Generated by Django 3.1.7 on 2021-05-04 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_auto_20210502_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstoqueEntrada',
            fields=[
            ],
            options={
                'verbose_name': 'estoque entrada',
                'verbose_name_plural': 'estoque entrada',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('estoque.estoque',),
        ),
        migrations.CreateModel(
            name='EstoqueSaida',
            fields=[
            ],
            options={
                'verbose_name': 'estoque saida',
                'verbose_name_plural': 'estoque saida',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('estoque.estoque',),
        ),
    ]
