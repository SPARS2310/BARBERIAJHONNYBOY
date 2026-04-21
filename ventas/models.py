from django.db import models
from django.utils import timezone

class Barbero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=15, help_text="Para notificaciones de WhatsApp")
    esta_activo = models.BooleanField(default=True, help_text="Desmarcar si el barbero ya no trabaja aquí")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Barberos"

class Servicio(models.Model):
    """Agregamos esta tabla para que la IA sepa qué servicios vendes y cuánto cuestan"""
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    duracion_minutos = models.IntegerField(default=30, help_text="Cuanto tarda el corte aprox")
    descripcion = models.TextField(blank=True, help_text="Ej: Incluye lavado y delineado de barba")

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Cita(models.Model):
    ESTADOS = [
        ('P', 'Pendiente (Agendada por WhatsApp)'),
        ('L', 'Llegó al local (En espera)'),
        ('C', 'Completada / Pagada'),
        ('N', 'No asistió'),
    ]
    
    cliente_nombre = models.CharField(max_length=100)
    cliente_telefono = models.CharField(max_length=15)
    barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE, related_name='citas')
    servicio_solicitado = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True)
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fecha_hora.strftime('%d/%m %H:%M')} - {self.cliente_nombre} con {self.barbero}"

    class Meta:
        # Evita que se agenden dos personas con el mismo barbero a la misma hora
        unique_together = ('barbero', 'fecha_hora')

class Venta(models.Model):
    METODOS = [('EF', 'Efectivo'), ('TJ', 'Tarjeta')]
    
    cita = models.OneToOneField(Cita, on_delete=models.SET_NULL, null=True, blank=True)
    barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)
    # Si viene de una cita, jalamos el servicio de allá, si no, se pone manual
    servicio_manual = models.CharField(max_length=100, blank=True, help_text="Solo si no hubo cita previa")
    monto = models.DecimalField(max_digits=7, decimal_places=2)
    metodo_pago = models.CharField(max_length=2, choices=METODOS)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fecha.strftime('%d/%m %H:%M')} - ${self.monto} - {self.barbero}"

class ConfiguracionBarberia(models.Model):
    """Esto es para que Gemini sepa el horario de Tijuana"""
    nombre_local = models.CharField(max_length=100, default="Barbería JhonnyBoy")
    hora_apertura = models.TimeField(default="10:00")
    hora_cierre = models.TimeField(default="20:00")
    mensaje_bienvenida = models.TextField(default="¡Hola! Bienvenido a JhonnyBoy. ¿Con quién te gustaría agendar?")

    def __str__(self):
        return self.nombre_local