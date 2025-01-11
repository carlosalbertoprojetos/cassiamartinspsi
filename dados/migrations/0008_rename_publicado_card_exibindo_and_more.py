# Generated by Django 4.2.11 on 2025-01-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0007_alter_abordagem_titulo_alter_apresentacao_sub_titulo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='publicado',
            new_name='exibindo',
        ),
        migrations.RenameField(
            model_name='indicesabordagem',
            old_name='publicado',
            new_name='exibindo',
        ),
        migrations.RenameField(
            model_name='subtopico',
            old_name='publicado',
            new_name='exibindo',
        ),
        migrations.RenameField(
            model_name='textosindiceabordagem',
            old_name='publicado',
            new_name='exibindo',
        ),
        migrations.AlterField(
            model_name='abordagem',
            name='atual',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='apresentacao',
            name='atual',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='atual',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='atual',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='topico',
            name='atual',
            field=models.BooleanField(default=True),
        ),
    ]