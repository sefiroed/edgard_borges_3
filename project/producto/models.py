from django.db import models

# Create your models here.


class ProductoCategoria(models.Model):
    """Categoría de productos"""
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        """Representa una instancia del modelo como una cadena de texto"""
        return self.nombre

    class Meta:
        """Verbose_name es el nombre con el que se representa en el panel de administración"""
        verbose_name = "categoría de productos"
        verbose_name_plural = "categorías de productos"
