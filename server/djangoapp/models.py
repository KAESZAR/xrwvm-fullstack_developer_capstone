from django.db import models  
from django.core.validators import MaxValueValidator, MinValueValidator 

class CarMake(models.Model):  
    name = models.CharField(max_length=100)  # Nombre de la marca  
    description = models.TextField(blank=True)  # Descripción de la marca  
    # Otros campos que se deseen incluir, por ejemplo:  
    country_of_origin = models.CharField(max_length=100, blank=True)  # País de origen  

    def __str__(self):  
        return self.name  # Retorna el nombre como representación de cadena  

class CarModel(models.Model):  
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Relación de muchos a uno  
    dealership_id = models.IntegerField()  # ID del concesionario  
    name = models.CharField(max_length=100)  # Nombre del modelo  
    CAR_TYPES = [  
        ('SEDAN', 'Sedan'),  
        ('SUV', 'SUV'),  
        ('WAGON', 'Wagon'),  
        # Agregar más opciones según sea necesario  
    ]  
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')  # Tipo de coche  
    year = models.DateField()  # Año del modelo (usamos DateField)  

    def __str__(self):  
        return f"{self.car_make} {self.name}"  # Retorna la marca y el nombre del modelo como representación de cadena 
