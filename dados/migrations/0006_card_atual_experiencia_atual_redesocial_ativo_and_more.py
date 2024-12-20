# Generated by Django 4.2.11 on 2024-11-06 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0005_card_texto_card_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='atual',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiencia',
            name='atual',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='redesocial',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='abordagem',
            name='atual',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='apresentacao',
            name='atual',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='topico',
            name='atual',
            field=models.BooleanField(default=False),
        ),
    ]
