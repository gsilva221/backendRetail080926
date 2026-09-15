from django.db import models
# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    disponibilidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class PrecioServcio(models.Model):
    servicio = models.OneToOneField(
        Servicio, 
        on_delete=models.CASCADE
        )
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2
        )
    decuento = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0.00
        )
    moneda = models.CharField(
        max_length=10, 
        default='CLP'
        )
    observacion = models.TextField(
        blank=True, 
        max_length=200
        )

    def __str__(self):
        return f"{self.servicio.nombre} - {self.precio} {self.moneda}"