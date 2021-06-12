from django.db import models

class Parroquia(models.Model):
    opciones_tipo_parroquia = (
        ('urbana', 'Urbana'),
        ('rural', 'Rural'),
        )

    nombre = models.CharField("Nombre de la parroquia", max_length=30)
    tipo = models.CharField(max_length=30, \
            choices=opciones_tipo_parroquia) 


    def __str__(self):
        return "Parroquia: %s - Tipo de parroquia: %s" % (
                self.nombre, 
                self.tipo)
    
class Barrio(models.Model):
    num_parques = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        )

    nombre = models.CharField("Nombre del barrio", max_length=30)
    num_viviendas = models.IntegerField("Numero de viviendas")
    num_parques = models.IntegerField("Numero de parques", choices = num_parques) 
    num_edificios = models.IntegerField("Numero de edificios")
    parroquia = models.ForeignKey(Parroquia, related_name='parroquias', 
            on_delete=models.CASCADE)


    def __str__(self):
        return "Barrio: %s - viviendas: %d - Parques: %d - Edificios: %d" % (
                self.nombre,
                self.num_viviendas,
                self.num_parques,
                self.num_edificios)