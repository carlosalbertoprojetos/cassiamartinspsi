# Generated by Django 4.2.11 on 2024-05-20 22:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0002_apresentacao_alter_telefone_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='apresentacao',
            name='foto',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='apresentacao/foto/'),
            preserve_default=False,
        ),
    ]
