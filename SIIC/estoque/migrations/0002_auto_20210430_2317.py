# Generated by Django 3.1.7 on 2021-05-01 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_auto_20210430_2135'),
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EstoquerItens',
            new_name='EstoqueItens',
        ),
    ]
