from rest_framework import serializers
from .models import Ruolo

class RuoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruolo 
        fields = ('pk', 'nome')