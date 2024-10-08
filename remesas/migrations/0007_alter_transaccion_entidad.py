# Generated by Django 5.0.6 on 2024-07-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remesas', '0006_alter_transaccion_num_comprobante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='entidad',
            field=models.CharField(choices=[('BANCOP S.A.', 'BANCOP S.A.'), ('Banco Atlas S.A.', 'Banco Atlas S.A.'), ('Banco BASA', 'Banco BASA'), ('Banco Continental S.A.E.C.A.', 'Banco Continental S.A.E.C.A.'), ('Banco Familiar S.A.E.C.A.', 'Banco Familiar S.A.E.C.A.'), ('Banco GNB - Paraguay', 'Banco GNB - Paraguay'), ('Banco Itaú Paraguay S.A.', 'Banco Itaú Paraguay S.A.'), ('Banco Nacional de Fomento (BNF)', 'Banco Nacional de Fomento (BNF)'), ('Banco Rio S.A.E.C.A', 'Banco Rio S.A.E.C.A'), ('COOPEDUC Ltda.', 'COOPEDUC Ltda.'), ('COPACONS Ltda.', 'COPACONS Ltda.'), ('Cooperativa 21 de Setiembre Ltda.', 'Cooperativa 21 de Setiembre Ltda.'), ('Cooperativa Alemán Concordia Ltda.', 'Cooperativa Alemán Concordia Ltda.'), ('Cooperativa Chortitzer Ltda.', 'Cooperativa Chortitzer Ltda.'), ('Cooperativa Coodeñe Ltda.', 'Cooperativa Coodeñe Ltda.'), ('Cooperativa Colonias Unidas Ltda.', 'Cooperativa Colonias Unidas Ltda.'), ('Cooperativa Coomecipar Ltda.', 'Cooperativa Coomecipar Ltda.'), ('Cooperativa de las Fuerzas Armadas de la Nación Ltda.', 'Cooperativa de las Fuerzas Armadas de la Nación Ltda.'), ('Cooperativa Fernheim Ltda.', 'Cooperativa Fernheim Ltda.'), ('Cooperativa Mborayhu Ltda.', 'Cooperativa Mborayhu Ltda.'), ('Cooperativa Mburicao Ltda.', 'Cooperativa Mburicao Ltda.'), ('Cooperativa Medalla Milagrosa Ltda.', 'Cooperativa Medalla Milagrosa Ltda.'), ('Cooperativa Mercado 4 Ltda.', 'Cooperativa Mercado 4 Ltda.'), ('Cooperativa Multiactiva 8 de Marzo Ltda.', 'Cooperativa Multiactiva 8 de Marzo Ltda.'), ('Cooperativa Naranjal Ltda.', 'Cooperativa Naranjal Ltda.'), ('Cooperativa Nazareth Ltda.', 'Cooperativa Nazareth Ltda.'), ('Cooperativa Neuland Ltda.', 'Cooperativa Neuland Ltda.'), ('Cooperativa Ñemby Ltda.', 'Cooperativa Ñemby Ltda.'), ('Cooperativa Raúl Peña Ltda.', 'Cooperativa Raúl Peña Ltda.'), ('Cooperativa San Ignacio', 'Cooperativa San Ignacio'), ('Cooperativa San Juan Bautista Ltda.', 'Cooperativa San Juan Bautista Ltda.'), ('Cooperativa Universitaria Ltda.', 'Cooperativa Universitaria Ltda.'), ('Cooperativa Ypacarai Ltda.', 'Cooperativa Ypacarai Ltda.'), ('Financiera Paraguayo Japonesa S.A.E.C.A', 'Financiera Paraguayo Japonesa S.A.E.C.A'), ('FINANCIERA FIC S.A.E.C.A.', 'FINANCIERA FIC S.A.E.C.A.'), ('Interfisa Banco', 'Interfisa Banco'), ('Solar Banco S.A.E.', 'Solar Banco S.A.E.'), ('Sudameris Bank S.A.E.C.A.', 'Sudameris Bank S.A.E.C.A.'), ('TIGO BANK', 'TIGO BANK'), ('TIGO-349', 'TIGO-349'), ('TIGO-722', 'TIGO-722'), ('TIGO-757', 'TIGO-757'), ('Tu Financiera', 'Tu Financiera'), ('Ueno', 'Ueno'), ('Visión Banco S.A.E.C.A.', 'Visión Banco S.A.E.C.A.'), ('WALLY-349', 'WALLY-349'), ('WALLY-722', 'WALLY-722'), ('WALLY-757', 'WALLY-757'), ('ZETA Banco', 'ZETA Banco'), ('ZIMPLE-349', 'ZIMPLE-349'), ('ZIMPLE-722', 'ZIMPLE-722'), ('ZIMPLE-757', 'ZIMPLE-757')], max_length=100),
        ),
    ]
