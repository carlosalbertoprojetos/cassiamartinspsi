# Generated by Django 4.2.11 on 2024-11-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0002_experiencia_grupoexperiencia_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='abordagem',
            name='atual',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apresentacao',
            name='atual',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='email',
            name='atual',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='atual',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='home',
            name='atual',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='indicesabordagem',
            name='atual',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='topico',
            name='atual',
            field=models.BooleanField(default=True),
        ),
    ]
