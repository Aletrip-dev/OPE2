# Generated by Django 2.0.13 on 2021-03-20 15:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='primeiro_nome',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Primeiro nome'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='sobrenome',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Sobrenome'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='data_exclusao',
            field=models.DateField(blank=True, null=True),
        ),
    ]
