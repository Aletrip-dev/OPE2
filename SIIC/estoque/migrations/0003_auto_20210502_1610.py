# Generated by Django 3.1.7 on 2021-05-02 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_auto_20210430_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='nf',
            field=models.PositiveIntegerField(default=1, verbose_name='Nota Fiscal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estoqueitens',
            name='estoque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estoques', to='estoque.estoque'),
        ),
    ]
