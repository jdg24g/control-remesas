# Generated by Django 5.0.6 on 2024-08-26 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remesas', '0008_transaccion_ultima_modificacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaccion',
            options={'verbose_name': 'Transacción', 'verbose_name_plural': 'Transacciones'},
        ),
    ]
