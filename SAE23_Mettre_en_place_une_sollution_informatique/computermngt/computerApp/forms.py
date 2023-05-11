from django import forms
from django.core.exceptions import ValidationError

class AddMachineForm(forms.Form) :
    nom = forms.CharField(required=True, label='Nom de la machine')
    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 32 :
            raise ValidationError( ("Erreur de format pour le champ nom"))
        return data


class AddPersonnelForm(forms.Form) :
    nom = forms.CharField(required=True, label='Nom de la personne')
    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 32 :
            raise ValidationError( ("Erreur de format pour le champ nom"))
        return data