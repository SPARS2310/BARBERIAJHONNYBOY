from django.contrib import admin
from .models import Barbero, Cita, Venta

# --- CONFIGURACIÓN DE BARBERO ---
@admin.register(Barbero)
class BarberoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono')
    search_fields = ('nombre',)

# --- CONFIGURACIÓN DE CITAS ---
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    # Esto permite ver la lista de citas de forma profesional
    list_display = ('cliente_nombre', 'barbero', 'servicio_solicitado', 'fecha_hora', 'estado')
    # Filtros laterales para que el dueño busque rápido por día o barbero
    list_filter = ('barbero', 'estado', 'fecha_hora')
    # Permite buscar clientes por nombre en la barrita de búsqueda
    search_fields = ('cliente_nombre', 'servicio_solicitado')
    # Ordenar por fecha, la más reciente primero
    ordering = ('-fecha_hora',)

# --- CONFIGURACIÓN DE VENTAS (INGRESOS) ---
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'barbero', 'servicio', 'monto', 'metodo_pago')
    list_filter = ('barbero', 'metodo_pago', 'fecha')
    readonly_fields = ('fecha',) 
    
    # Esto hará que el dueño vea el total de dinero al final de la lista (opcional pero muy útil)
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)