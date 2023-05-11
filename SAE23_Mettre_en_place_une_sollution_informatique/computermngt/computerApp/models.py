from django.db import models
from datetime import datetime

# Create your models here.

class Machine(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom= models.CharField(max_length= 6)
    maintenanceDate = models.DateField(default=datetime.now())
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')
    def __str__(self): return str(self.id) + " -> " + self.nom
    def get_name(self): return str(self.id) + " " + self.nom




class Personnel(models.Model):
    ROLE = (
        ('utilisateur', ('utilisateur - personnel ')),
        ('administrateur', ('administrateur - Réseaux')),  
    )

    id = models.AutoField(
        primary_key=True)
    nom= models.CharField(
        max_length= 10)
    prenom= models.CharField(
        max_length= 10)
    pers = models.CharField(max_length=64, choices=ROLE, default='utilisateur')   

    def __str__(self):
        return str(self.id) + " -> " + self.nom + " " + self.prenom