from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Utente
from .serializers import *

from ruolo.models import Ruolo
from utente_ruolo.models import UtenteRuolo

@api_view(['GET', 'POST'])
def utenti_list(request):
    if request.method == 'GET':
        data = []
        ruolo = Ruolo.objects.get(nome='AUROR')
        if ruolo:
            utenti_ruolo = UtenteRuolo.objects.filter(fkRuolo=ruolo)
            if utenti_ruolo:
                for ur in utenti_ruolo:
                    data.append(ur.fkUtente)
        
        serializer = UtenteSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UtenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def utenti_detail(request, pk):
    try:
        utente = Utente.objects.get(pk=pk)
    except Utente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = UtenteSerializer(utente, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        utente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)