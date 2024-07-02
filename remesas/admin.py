from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .models import Cliente, Transaccion
from django.core.exceptions import ValidationError


class MonthListFilter(admin.SimpleListFilter):
    title = _("mes")
    parameter_name = "month"

    def lookups(self, request, model_admin):
        months = [
            (i, timezone.now().replace(month=i).strftime("%B")) for i in range(1, 13)
        ]
        return months

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(agregado__month=self.value())
        return queryset


class YearListFilter(admin.SimpleListFilter):
    title = _("año")
    parameter_name = "year"

    def lookups(self, request, model_admin):
        current_year = timezone.now().year
        years = [(i, str(i)) for i in range(current_year - 1, current_year + 1)]
        return years

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(agregado__year=self.value())
        return queryset


class MultiSelectEntityFilter(admin.SimpleListFilter):
    title = _("entidad")
    parameter_name = "entidad"

    def lookups(self, request, model_admin):
        entidades = set(Transaccion.objects.values_list("entidad", flat=True))
        return [(entidad, entidad) for entidad in entidades]

    def queryset(self, request, queryset):
        if self.value():
            entidades = self.value()
            return queryset.filter(entidad__in=entidades)
        return queryset

    def value(self):
        value = super().value()
        return value.split(",") if value else []


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

    def clean_cedula(self):
        cedula = self.cleaned_data.get("cedula")
        if (
            cedula
            and Cliente.objects.filter(cedula=cedula)
            .exclude(pk=self.instance.pk)
            .exists()
        ):
            raise ValidationError("La cédula ya existe.")
        return cedula


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = "__all__"

    def clean_num_comprobante(self):
        num_comprobante = self.cleaned_data.get("num_comprobante")
        if (
            num_comprobante
            and Transaccion.objects.filter(num_comprobante=num_comprobante).exists()
        ):
            raise ValidationError("El número de comprobante ya existe.")
        return num_comprobante


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["cedula", "nombre", "apellido", "whatsapp"]
    search_fields = ["cedula", "nombre", "apellido"]


@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    form = TransaccionForm
    list_display = [
        "cliente",
        "monto",
        "estado",
        "caja",
        "imagen_comprobante_preview",
        "cliente_whatsapp",
    ]
    list_filter = ["caja","estado", MultiSelectEntityFilter, YearListFilter, MonthListFilter]
    search_fields = [
        "cliente__cedula",
        "cliente__nombre",
        "cliente__apellido",
        "entidad",
    ]
    autocomplete_fields = ["cliente"]

    def imagen_comprobante_preview(self, obj):
        if obj.imagen_comprobante:
            return format_html(
                '<a href="{0}" class="preview-link" target="_blank" data-toggle="modal" data-target="#comprobanteModal"><img src="{0}" width="50" height="50" /></a>',
                obj.imagen_comprobante.url,
            )
        return "Sin Foto"

    imagen_comprobante_preview.short_description = "Comprobante"

    def cliente_whatsapp(self, obj):
        return format_html(
            '<a href="https://wa.me/{0}"target="_blank">Enviar Whatsapp</a>',
            obj.cliente.whatsapp,
        )

    actions = ["marcar_aprobadas", "marcar_rechazadas", "marcar_pendientes","marcar_enviados","marcarComoGiro", "marcarComoInterfisa"]

    def marcar_aprobadas(self, request, queryset):
        updated = queryset.update(estado="A")
        self.message_user(
            request, f"Se marcaron como Aprobadas {updated} transacciones."
        )

    marcar_aprobadas.short_description = _("Marcar como Aprobadas")

    def marcar_rechazadas(self, request, queryset):
        updated = queryset.update(estado="R")
        self.message_user(
            request, f"Se marcaron como Rechazadas {updated} transacciones."
        )

    marcar_rechazadas.short_description = _("Marcar como Rechazadas")

    def marcar_pendientes(self, request, queryset):
        updated = queryset.update(estado="P")
        self.message_user(
            request, f"Se marcaron como Pendientes {updated} transacciones."
        )

    marcar_pendientes.short_description = _("Marcar como Pendientes")

    def marcar_enviados(self, request,queryset):
        updated = queryset.update(estado="E")
        self.message_user(
            request, f"Se marcaron como Enviados {updated} transacciones."
        )
    marcar_enviados.short_description = _("Marcar como Enviados")

    def marcarComoGiro(self,request, queryset):
        updated = queryset.update(caja="G")
        self.message_user(
            request, f"Se marcaron como Giro {updated} transacciones."
        )
    marcarComoGiro.short_description = _("Marcar como Giro")

    def marcarComoInterfisa(self, request, queryset):
        updated = queryset.update(caja="I")
        self.message_user(
            request, f"Se marcaron como Interfisa {updated} transacciones."
        )
    marcarComoInterfisa.short_description = _("Marcar como Interfisa")

admin.site.site_header = "PLAYNET"
admin.site.site_title = "PLAYNET"
admin.site.index_title = "Bienvenido a la Página de Administración"
