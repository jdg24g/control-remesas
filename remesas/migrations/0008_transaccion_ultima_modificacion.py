# Generated by Django 5.0.6 on 2024-08-05 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remesas', '0007_alter_transaccion_entidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='ultima_modificacion',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
