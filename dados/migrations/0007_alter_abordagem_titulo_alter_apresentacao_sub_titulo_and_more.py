# Generated by Django 4.2.11 on 2024-11-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0006_card_atual_experiencia_atual_redesocial_ativo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abordagem',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='apresentacao',
            name='sub_titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='apresentacao',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='home',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='indicesabordagem',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='subtopico',
            name='sub_titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='textosindiceabordagem',
            name='sub_titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='topico',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]
