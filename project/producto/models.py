from django.db import models

# Create your models here.


# class InstrumentosDeCuerdas(models.Model):
#     """Modelo de instrumentos de cuerdas"""
#     nombre = models.CharField(max_length=200, unique=True)
#     precio = models.DecimalField(max_digits=10, decimal_places=2)
#     descripcion = models.TextField(
#         max_length=250, null=True, blank=True, verbose_name="descripción")
#     categoria = models.ForeignKey(
#         'ProductoCategoria', on_delete=models.SET_NULL, null=True, blank=True)
#     imagen = models.ImageField(
#         upload_to='instrumentos_de_cuerdas/', null=True, blank=True)

#     def __str__(self):
#         """Representa una instancia del modelo como una cadena de texto"""
#         return self.nombre


# class ProductoCategoria(models.Model):
#     """Categoría de productos"""
#     nombre = models.CharField(max_length=200, unique=True)
#     descripcion = models.CharField(
#         max_length=250, null=True, blank=True, verbose_name="descripción")

#     def __str__(self):
#         """Representa una instancia del modelo como una cadena de texto"""
#         return self.nombre

#     class Meta:
#         """Verbose_name es el nombre con el que se representa en el panel de administración"""
#         verbose_name = "categoría de productos"
#         verbose_name_plural = "categorías de productos"

class InstrumentoAire(models.Model):
    descripcion = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        return self.descripcion


class InstrumentoCuerdas(models.Model):
    descripcion = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        return self.descripcion


class Instrumento(models.Model):
    nombre = models.CharField(max_length=200)
    instrumentocuerdas = models.ForeignKey(
        InstrumentoCuerdas, on_delete=models.SET_NULL, null=True, blank=True)
    instrumentoaire = models.ForeignKey(
        InstrumentoAire, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre
