# Generated by Django 4.2.11 on 2024-06-09 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0007_alter_indice_options_alter_indiceabordagem_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Endereços',
            },
        ),
    ]
