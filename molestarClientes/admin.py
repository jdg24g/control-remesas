from django.contrib import admin
from .models import Formulario,Tecnico



@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display = [
        'tecnico_instalador','cliente', 'fecha_incluido'
    ]

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = [
        'nombre', 'tec_id'
    ]