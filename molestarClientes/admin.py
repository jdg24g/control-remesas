from django.contrib import admin
from .models import Formulario,Tecnico



@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display = [
        'estado','tecnico_instalador','cliente','get_cliente_whatsapp', 'fecha_incluido'
    ]
    search_fields = ["cliente__cedula", "cliente__nombre", "cliente__apellido"]
    autocomplete_fields = ["cliente"]
    list_filter = ["tecnico_instalador", "estado"]

    def get_cliente_whatsapp(self, obj):
        return obj.cliente.whatsapp
    get_cliente_whatsapp.short_description = 'WhatsApp del cliente'

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = [
        'nombre', 'tec_id'
    ]