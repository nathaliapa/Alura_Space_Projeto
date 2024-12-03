# Generated by Django 4.1 on 2024-11-30 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALAXIA', 'Galaxia'), ('pLANETA', 'Planeta')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.CharField(max_length=150),
        ),
    ]
