# Generated by Django 4.2.11 on 2025-01-23 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0010_alter_apresentacao_foto_alter_card_imagem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topico',
            options={'verbose_name_plural': '5 Atualidades'},
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='atual',
        ),
    ]
