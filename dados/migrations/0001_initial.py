# Generated by Django 4.2.11 on 2024-05-20 22:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Emails',
            },
        ),
        migrations.CreateModel(
            name='RedeSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('icone', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=14)),
            ],
            options={
                'verbose_name_plural': 'Telefones',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('texto', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('foto', models.ImageField(upload_to='home/foto/')),
                ('letreiro', models.JSONField(blank=True, null=True)),
                ('redes_sociais', models.ManyToManyField(to='dados.redesocial')),
            ],
            options={
                'verbose_name_plural': 'Home Page',
            },
        ),
    ]
