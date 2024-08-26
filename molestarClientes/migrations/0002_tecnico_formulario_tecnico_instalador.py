# Generated by Django 5.0.6 on 2024-08-26 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('molestarClientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('tec_id', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Tecnico',
                'verbose_name_plural': 'Tecnicos',
            },
        ),
        migrations.AddField(
            model_name='formulario',
            name='tecnico_instalador',
            field=models.CharField(default='No especificado', max_length=100, verbose_name='Técnico instalador'),
        ),
    ]
