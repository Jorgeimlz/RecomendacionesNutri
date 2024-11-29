from django.db import models
from ingredientes.models import Ingrediente
from tipos_recetas.models import TipoReceta

class Receta(models.Model):
    """
    Modelo para representar una receta.
    """
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)
    tiempo_preparacion = models.PositiveIntegerField()
    tiempo_coccion = models.PositiveIntegerField()
    porciones = models.PositiveIntegerField(default=1)
    popularidad = models.IntegerField(default=0)
    tipo = models.ForeignKey(TipoReceta, on_delete=models.SET_NULL, null=True, related_name="recetas")  # Relación con TipoReceta
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    ingredientes = models.ManyToManyField(
        Ingrediente,
        through='receta_ingrediente.RecetaIngrediente',
        related_name='recetas'
    )  # Relación ManyToMany con ingredientes a través de RecetaIngrediente

    def __str__(self):
        return self.nombre
    
    @property
    def valores_nutricionales(self):
        """
        Calcula los valores nutricionales totales de la receta considerando las unidades de los ingredientes.
        """
        total_calorias = 0
        total_proteinas = 0
        total_carbohidratos = 0
        total_grasas = 0

        for receta_ingrediente in self.receta_ingredientes.all():
            cantidad = receta_ingrediente.cantidad
            unidad = receta_ingrediente.unidad  # e.g., gramos, tazas, piezas

            # Convertir unidades si es necesario (asumimos que calorías son por 100 gramos)
            if unidad == 'gramos':
                factor = cantidad / 100  # Por 100 gramos
            elif unidad == 'kilogramos':
                factor = (cantidad * 1000) / 100
            else:
                # Manejar otras unidades o asumir 1:1 si no se especifica
                factor = cantidad / 100

            ingrediente = receta_ingrediente.ingrediente
            total_calorias += ingrediente.calorias * factor
            total_proteinas += ingrediente.proteinas * factor
            total_carbohidratos += ingrediente.carbohidratos * factor
            total_grasas += ingrediente.grasas * factor

        return {
            "calorias": total_calorias,
            "proteinas": total_proteinas,
            "carbohidratos": total_carbohidratos,
            "grasas": total_grasas,
        }
