from django.db import models
from datetime import datetime

class Trainer(models.Model):
    name = models.CharField(max_length=50, null = False)
    last_name = models.CharField(max_length=50, null = False)
    birth_date = models.DateField(null = False)
    level = models.IntegerField(default = 1)
    details = models.TextField(null = False)
    picture = models.ImageField(upload_to='trainer_images')

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'

class Pokemon (models.Model): #clase nombre de la tabla
    name = models.CharField(max_length= 30, null=False)
    POKEMON_TYPES ={
        ('A', 'AGUA'),
        ('F', 'FUEGO'),
        ('T', 'TIERRA'),
        ('P', 'PLANTA'),
        ('E', 'ELÉCTRICO'),
    }
    type = models.CharField(max_length= 30, choices=POKEMON_TYPES, null=False) #CHOICES ES PARA UN SELECTOR DE UN CAMPO DECLARADO
    weight = models.DecimalField(null = False, default=1, max_digits=4, decimal_places=2) 
    height = models.DecimalField(null = False, default=1, max_digits=4, decimal_places=2)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pokemon_images')
    
    def __str__(self) -> str:
        return self.name
    