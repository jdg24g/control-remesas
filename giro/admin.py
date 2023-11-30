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
        'cobrado',
        'cliente',
        'monto',
        'metodo_DePago',
        'display_transaccion_img',
    )
    
    def cobrado(self, obj):
        if obj.estado:
            return 'SI'
        else:
            return 'NO'

    def display_transaccion_img(self, obj):
        if obj.transaccion_img:
            return format_html(f'<a href="{obj.transaccion_img.url}" target="_blank">COMPROBANTE</a>')
        else:
            return 'SIN COMPROBANTE'
    
    display_transaccion_img.short_description = 'Transacción Imagen'


admin.site.register(Cliente)
admin.site.register(Transaccion,transaccionAdmin) 