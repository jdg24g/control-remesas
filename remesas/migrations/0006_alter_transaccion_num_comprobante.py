# Generated by Django 5.0.6 on 2024-07-02 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remesas', '0005_alter_cliente_cedula_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='num_comprobante',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
