# Generated by Django 5.0.2 on 2024-03-27 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repuestosalinstante', '0004_rename_país_origen_marca_pais_origen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='marca',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['nombre']},
        ),
    ]
