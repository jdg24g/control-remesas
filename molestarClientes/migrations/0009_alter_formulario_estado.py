# Generated by Django 5.0.6 on 2024-08-28 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('molestarClientes', '0008_alter_formulario_calidad_instalacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='estado',
            field=models.IntegerField(choices=[(1, 'Pendiente'), (2, 'Terminado'), (3, 'Sin Respuesta')], default=1),
        ),
    ]
