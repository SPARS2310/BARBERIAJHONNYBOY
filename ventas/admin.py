from django.contrib import admin
from .models import Barbero, Cita, Venta, Servicio, ConfiguracionBarberia

# --- CONFIGURACIÓN DE BARBERO ---
@admin.register(Barbero)
class BarberoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'esta_activo') 
    list_filter = ('esta_activo',)
    search_fields = ('nombre',)

# --- CONFIGURACIÓN DE SERVICIOS ---
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'duracion_minutos')
    search_fields = ('nombre',)

# --- CONFIGURACIÓN DE CITAS ---
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    # Aquí estaba el error: cambié 'servicio' por 'servicio_solicitado'
    list_display = ('cliente_nombre', 'barbero', 'servicio_solicitado', 'fecha_hora', 'estado')
    list_filter = ('barbero', 'estado', 'fecha_hora')
    search_fields = ('cliente_nombre', 'cliente_telefono')
    ordering = ('-fecha_hora',)

# --- CONFIGURACIÓN DE VENTAS ---
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'barbero', 'monto', 'metodo_pago')
    list_filter = ('barbero', 'metodo_pago', 'fecha')
    readonly_fields = ('fecha',)

# --- CONFIGURACIÓN DEL LOCAL (HORARIOS) ---
@admin.register(ConfiguracionBarberia)
class ConfiguracionBarberiaAdmin(admin.ModelAdmin):
    list_display = ('nombre_local', 'hora_apertura', 'hora_cierre')