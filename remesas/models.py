from django.db import models
from django.core.exceptions import ValidationError


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    cedula = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)

    def clean(self):
        if Cliente.objects.filter(cedula=self.cedula).exists():
            raise ValidationError("Cedula ya existe")

    def __str__(self):
        return f"{self.cedula} {self.nombre.upper()} {self.apellido.upper()}"


class Transaccion(models.Model):
    entidades = [
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
        (
            "Cooperativa de las Fuerzas Armadas de la Nación Ltda.",
            "Cooperativa de las Fuerzas Armadas de la Nación Ltda.",
        ),
        ("Cooperativa Fernheim Ltda.", "Cooperativa Fernheim Ltda."),
        ("Cooperativa Mborayhu Ltda.", "Cooperativa Mborayhu Ltda."),
        ("Cooperativa Mburicao Ltda.", "Cooperativa Mburicao Ltda."),
        ("Cooperativa Medalla Milagrosa Ltda.", "Cooperativa Medalla Milagrosa Ltda."),
        ("Cooperativa Mercado 4 Ltda.", "Cooperativa Mercado 4 Ltda."),
        (
            "Cooperativa Multiactiva 8 de Marzo Ltda.",
            "Cooperativa Multiactiva 8 de Marzo Ltda.",
        ),
        ("Cooperativa Naranjal Ltda.", "Cooperativa Naranjal Ltda."),
        ("Cooperativa Nazareth Ltda.", "Cooperativa Nazareth Ltda."),
        ("Cooperativa Neuland Ltda.", "Cooperativa Neuland Ltda."),
        ("Cooperativa Ñemby Ltda.", "Cooperativa Ñemby Ltda."),
        ("Cooperativa Raúl Peña Ltda.", "Cooperativa Raúl Peña Ltda."),
        ("Cooperativa San Ignacio", "Cooperativa San Ignacio"),
        ("Cooperativa San Juan Bautista Ltda.", "Cooperativa San Juan Bautista Ltda."),
        ("Cooperativa Universitaria Ltda.", "Cooperativa Universitaria Ltda."),
        ("Cooperativa Ypacarai Ltda.", "Cooperativa Ypacarai Ltda."),
        (
            "Financiera Paraguayo Japonesa S.A.E.C.A",
            "Financiera Paraguayo Japonesa S.A.E.C.A",
        ),
        ("FINANCIERA FIC S.A.E.C.A.", "FINANCIERA FIC S.A.E.C.A."),
        ("Interfisa Banco", "Interfisa Banco"),
        ("Solar Banco S.A.E.", "Solar Banco S.A.E."),
        ("Sudameris Bank S.A.E.C.A.", "Sudameris Bank S.A.E.C.A."),
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

    estado = [
        ("P", "Pendiente"),
        ("A", "Aprobado"),
        ("R", "Rechazado"),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    entidad = models.CharField(choices=entidades,max_length=100)
    remitente = models.CharField(
        max_length=50, default="El cliente es el remitente", blank=True, null=True
    )
    num_comprobante = models.CharField(max_length=50, blank=True, null=True)
    agregado = models.DateTimeField(auto_now_add=True)
    monto = models.PositiveIntegerField(default=0)
    imagen_comprobante = models.ImageField(
        upload_to="comprobantes", blank=True, null=True
    )
    estado = models.CharField(max_length=1, choices=estado, default="P")
    observacion = models.TextField(blank=True, null=True)

    def clean(self):
        if self.num_comprobante:
            if Transaccion.objects.filter(
                num_comprobante=self.num_comprobante
            ).exists():
                raise ValidationError(
                    {"num_comprobante": "El número de comprobante ya existe."}
                )

    def __str__(self):
        return f"{self.cliente}"
