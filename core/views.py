from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.serializer import *
from core.models import *

from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import generics


class QuartoList(generics.ListCreateAPIView):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    name = 'quarto-list'


class QuartoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    name = 'quarto-detail'


class ReservaList(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSeriaizer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    name = 'reserva-list'


class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSeriaizer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    name = 'reserva-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'Quarto': reverse(QuartoList.name, request=request),
            'Reserva': reverse(ReservaList.name, request=request),
        })
