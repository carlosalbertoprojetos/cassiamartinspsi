# Generated by Django 4.2.11 on 2025-01-12 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0009_alter_abordagem_options_alter_apresentacao_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apresentacao',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='apresentacao/foto/'),
        ),
        migrations.AlterField(
            model_name='card',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='card/foto/'),
        ),
    ]