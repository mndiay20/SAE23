from django import forms
from django.db import models
from django.core.exceptions import ValidationError
import ipaddress
from .models import Personnel



class AddMachineForm(forms.Form) :
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

    nom = forms.CharField(label='Nom de la machine')
    mach = forms.ChoiceField(choices=TYPE, initial='PC', label='Type de la machine')
    reseau = forms.ChoiceField(choices=RESEAU_MACHINE, label='Nom du réseau')
    ip = forms.GenericIPAddressField(label='Adresse ip de la machine')
    utilisateur = forms.ModelChoiceField(queryset=Personnel.objects.all(), label='Utilisateur')



    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 32 :
            raise ValidationError( ("Erreur de format pour le champ nom"))
        return data

    
    def clean_id(self):
        data = self.cleaned_data["id"]
        if len(data) > 60:
            raise ValidationError("Erreur de format")
        return data
    
    def clean_ip(self):
        data = self.cleaned_data["ip"]
        try:
            ipaddress.ip_address(data)
        except ValueError:
            raise forms.ValidationError("Erreur de format")
        return data   
   
    def clean_reseau(self):
        data = self.cleaned_data["reseau"]
        if len(data) > 60:
            raise forms.ValidationError("Erreur de format")
        return data

    def clean_type(self):
        data = self.cleaned_data["mach"]
        if len(data) > 40:
            raise ValidationError("Erreur de format")
        return data
    





class AddPersonnelForm(forms.Form) :
    ROLE = (
        ('utilisateur', ('utilisateur - personnel ')),
        ('administrateur', ('administrateur - Réseaux')),  
    )
    nom = forms.CharField(label='Nom de la personne')
    prenom= forms.CharField(label='Prénom de la personne')
    pers = forms.ChoiceField(choices=ROLE, initial='utilisateur', label='Fonction de la personne')   

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 32 :
            raise ValidationError( ("Erreur de format pour le champ nom"))
        return data

    def clean_prenom(self):
        data = self.cleaned_data["prenom"]
        if len(data) > 32 :
            raise ValidationError( ("Erreur de format pour le champ prenom"))
        return data

    def clean_pers(self):
        data = self.cleaned_data["pers"]
        if len(data) > 32 :
            raise ValidationError( ("Erreur de format pour le champ fonctio"))
        return data