# Generated by Django 3.1.7 on 2021-03-02 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=150)),
                ('funcao_usuario', models.CharField(max_length=50, verbose_name='Função')),
                ('nivel_usuario', models.CharField(max_length=50, verbose_name='Nível')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_pedido', models.DecimalField(decimal_places=2, max_digits=6)),
                ('data_pedido', models.DateField(auto_now=True)),
                ('usuario_pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.usuario')),
            ],
        ),
    ]
