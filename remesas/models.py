# models.py
from django.db import models
from django.core.exceptions import ValidationError

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    cedula = models.CharField(max_length=20, unique=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        nombre = self.nombre.upper() if self.nombre else ""
        apellido = self.apellido.upper() if self.apellido else ""
        return f"{nombre} {apellido}"
        

class Transaccion(models.Model):
    ENTIDADES = [
        ("BANCOP S.A.", "BANCOP S.A."),
        ("Banco Atlas S.A.", "Banco Atlas S.A."),
        ("Banco BASA", "Banco BASA"),
        ("Banco Continental S.A.E.C.A.", "Banco Continental S.A.E.C.A."),
        ("Banco Familiar S.A.E.C.A.", "Banco Familiar S.A.E.C.A."),
        ("Banco GNB - Paraguay", "Banco GNB - Paraguay"),
        ("Banco Itaú Paraguay S.A.", "Banco Itaú Paraguay S.A."),
        ("Banco Nacional de Fomento (BNF)", "Banco Nacional de Fomento (BNF)"),
        ("Banco Rio S.A.E.C.A", "Banco Rio S.A.E.C.A"),
        ("COOPEDUC Ltda.", "COOPEDUC Ltda."),
        ("COPACONS Ltda.", "COPACONS Ltda."),
        ("Cooperativa 21 de Setiembre Ltda.", "Cooperativa 21 de Setiembre Ltda."),
        ("Cooperativa Alemán Concordia Ltda.", "Cooperativa Alemán Concordia Ltda."),
        ("Cooperativa Chortitzer Ltda.", "Cooperativa Chortitzer Ltda."),
        ("Cooperativa Coodeñe Ltda.", "Cooperativa Coodeñe Ltda."),
        ("Cooperativa Colonias Unidas Ltda.", "Cooperativa Colonias Unidas Ltda."),
        ("Cooperativa Coomecipar Ltda.", "Cooperativa Coomecipar Ltda."),
        ("Cooperativa de las Fuerzas Armadas de la Nación Ltda.", "Cooperativa de las Fuerzas Armadas de la Nación Ltda."),
        ("Cooperativa Fernheim Ltda.", "Cooperativa Fernheim Ltda."),
        ("Cooperativa Mborayhu Ltda.", "Cooperativa Mborayhu Ltda."),
        ("Cooperativa Mburicao Ltda.", "Cooperativa Mburicao Ltda."),
        ("Cooperativa Medalla Milagrosa Ltda.", "Cooperativa Medalla Milagrosa Ltda."),
        ("Cooperativa Mercado 4 Ltda.", "Cooperativa Mercado 4 Ltda."),
        ("Cooperativa Multiactiva 8 de Marzo Ltda.", "Cooperativa Multiactiva 8 de Marzo Ltda."),
        ("Cooperativa Naranjal Ltda.", "Cooperativa Naranjal Ltda."),
        ("Cooperativa Nazareth Ltda.", "Cooperativa Nazareth Ltda."),
        ("Cooperativa Neuland Ltda.", "Cooperativa Neuland Ltda."),
        ("Cooperativa Ñemby Ltda.", "Cooperativa Ñemby Ltda."),
        ("Cooperativa Raúl Peña Ltda.", "Cooperativa Raúl Peña Ltda."),
        ("Cooperativa San Ignacio", "Cooperativa San Ignacio"),
        ("Cooperativa San Juan Bautista Ltda.", "Cooperativa San Juan Bautista Ltda."),
        ("Cooperativa Universitaria Ltda.", "Cooperativa Universitaria Ltda."),
        ("Cooperativa Ypacarai Ltda.", "Cooperativa Ypacarai Ltda."),
        ("Financiera Paraguayo Japonesa S.A.E.C.A", "Financiera Paraguayo Japonesa S.A.E.C.A"),
        ("FINANCIERA FIC S.A.E.C.A.", "FINANCIERA FIC S.A.E.C.A."),
        ("Interfisa Banco", "Interfisa Banco"),
        ("Solar Banco S.A.E.", "Solar Banco S.A.E."),
        ("Sudameris Bank S.A.E.C.A.", "Sudameris Bank S.A.E.C.A."),
        ("TIGO BANK","TIGO BANK"),
        ("TIGO-349","TIGO-349"),
        ("TIGO-722","TIGO-722"),
        ("TIGO-757","TIGO-757"),
        ("Tu Financiera", "Tu Financiera"),
        ("Ueno", "Ueno"),
        ("Visión Banco S.A.E.C.A.", "Visión Banco S.A.E.C.A."),
        ("WALLY-349", "WALLY-349"),
        ("WALLY-722", "WALLY-722"),
        ("WALLY-757", "WALLY-757"),
        ("ZETA Banco", "ZETA Banco"),
        ("ZIMPLE-349", "ZIMPLE-349"),
        ("ZIMPLE-722", "ZIMPLE-722"),
        ("ZIMPLE-757", "ZIMPLE-757"),
    ]
    CAJAS = [
        ("G", "Giro"),
        ("I","Interfisa")
    ]
    ESTADOS = [
        ("P", "Pendiente"),
        ("A", "Aprobado"),
        ("E", "Enviado"),
        ("R", "Rechazado"),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    caja = models.CharField(choices=CAJAS, max_length=50, blank=True, null=True)
    entidad = models.CharField(choices=ENTIDADES, max_length=100)
    remitente = models.CharField(max_length=50, default="El cliente es el remitente", blank=True, null=True)
    num_comprobante = models.CharField(max_length=50, blank=True, null=True)
    agregado = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(null=True,blank=True,auto_now=True)
    monto = models.PositiveIntegerField(default=0)
    imagen_comprobante = models.ImageField(upload_to="comprobantes", blank=True, null=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default="P")
    observacion = models.TextField(blank=True, null=True)

    def clean(self):
        if self.num_comprobante:
            transaccion_qs = Transaccion.objects.filter(num_comprobante=self.num_comprobante)
            if self.pk:
                transaccion_qs = transaccion_qs.exclude(pk=self.pk)
                print(transaccion_qs)
            if transaccion_qs.exists():
                print(transaccion_qs)
                raise ValidationError({"num_comprobante": "El número de comprobante ya existe."})

    def __str__(self):
        return f"{self.cliente}"