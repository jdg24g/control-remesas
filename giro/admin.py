from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Cliente,Transaccion
from django.utils.html import format_html
# Register your models here.


class transaccionAdmin(admin.ModelAdmin):
    """admin model Entry"""
    list_display = (
        'id',
        'cliente',
        'monto',
        'metodo_DePago',
        'display_transaccion_img',
    )
    
    def display_transaccion_img(self, obj):
        if obj.transaccion_img:
            return format_html(f'<a href="{obj.transaccion_img.url}" target="_blank">COMPROBANTE</a>')
        else:
            return 'SIN COMPROBANTE'
    
    display_transaccion_img.short_description = 'Transacción Imagen'
    
    @staticmethod
    def export_to_csv(modeladmin, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="transacciones.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID', 'Cliente', 'Monto', 'Método de Pago', 'Imagen URL'])

        for obj in queryset:
            writer.writerow([obj.id, obj.cliente, obj.monto, obj.metodo_DePago, obj.transaccion_img.url if obj.transaccion_img else ''])

        return response

    export_to_csv.short_description = "Exportar a CSV"


admin.site.register(Cliente)
admin.site.register(Transaccion,transaccionAdmin) 