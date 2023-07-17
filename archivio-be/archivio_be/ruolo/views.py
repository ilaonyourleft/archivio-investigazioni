from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Ruolo
from .serializers import *

@api_view(['GET'])
def ruoli_list(request):
    if request.method == 'GET':
        ruoli = Ruolo.objects.all()
        if ruoli:
            serializer = RuoloSerializer(ruoli, context={'request': request}, many=True)
            return Response(serializer.data)