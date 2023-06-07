from datetime import datetime
from django.db import models
# Create your models here.

class Machine(models.Model):
    RESEAU_MACHINE = (
        ('Filial', 'Filial - 192.168.0.0'),
        ('FAI', 'FAI - 10.10.10.0'),
        ('DMZ', 'DMZ - 172.16.0.0'),
    )

    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
        ('Rooter', ('Rooter - To maintains and connect LAN')),
    )

    id = models.AutoField(
        primary_key=True, editable=False)
    nom= models.CharField(
        max_length= 6)
    maintenanceDate = models.DateField(
        default=datetime.now())
    mach = models.CharField(
        max_length=200, choices=TYPE, default='PC')
    reseau = models.CharField(
        max_length=200, choices=RESEAU_MACHINE, default='FAI')
    ip = models.GenericIPAddressField(
        null=True)
    utilisateur = models.ForeignKey(
      'computerApp.Personnel', on_delete=models.SET_NULL, null=True)
    


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
    pers = models.CharField(
        max_length=64, choices=ROLE, default='utilisateur')   
    
    def __str__(self):
        return str(self.id) + " -> " + self.nom + " " + self.prenom



