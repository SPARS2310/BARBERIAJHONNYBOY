from django.db import models

class Barbero(models.Model):
    # Esto permite que el patrón agregue o quite barberos desde el admin
    # sin tener que tocar el código de las "choices"
    nombre = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=15, help_text="Para notificaciones de WhatsApp")

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    ESTADOS = [
        ('P', 'Pendiente (Agendada por WhatsApp)'),
        ('L', 'Llegó al local (En espera)'),
        ('C', 'Completada / Pagada'),
        ('N', 'No asistió'),
    ]
    
    cliente_nombre = models.CharField(max_length=100)
    cliente_telefono = models.CharField(max_length=15)
    barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)
    servicio_solicitado = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')

    def __str__(self):
        return f"{self.fecha_hora.strftime('%d/%m %H:%M')} - {self.cliente_nombre} con {self.barbero}"

class Venta(models.Model):
    METODOS = [('EF', 'Efectivo'), ('TJ', 'Tarjeta')]
    
    # Relacionamos la venta con la cita (si existe)
    cita = models.OneToOneField(Cita, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Mantenemos tus campos originales para no romper lo que ya tenías
    barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)
    servicio = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=7, decimal_places=2)
    metodo_pago = models.CharField(max_length=2, choices=METODOS)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fecha.strftime('%d/%m %H:%M')} - ${self.monto} - {self.barbero}"