from rest_framework import serializers
from APIREST.models import *

class VentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventes
        fields = [
            'pk',
            'designation',
            'prix',
            'date',
            
        ]


class DepensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depenses
        fields = [
            'pk',
            'designation',
            'prix',
            'date',
            
        ]


class PretsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prets
        fields = [
            'pk',
            'nomclient',
            'libelle',
            'montant',
            'date',
            
        ]   

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'pk',
            'nom',
            'numero',
            'date',
            
            
        ]              

        read_only_fields=['prix']
        read_only_fields=['nomclient']
        read_only_fields=['numero']

# ce fichier nous permet de convertir en json et de mettre des conditions de validations        
#convertir en JSON
# Validation des données
    
    def validate_designation(self, value):
        qs = Ventes.objects.filter(designation__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("title already exist please choice another one")
        return value  
