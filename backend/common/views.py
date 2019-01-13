from django.shortcuts import render

from rest_framework import viewsets, response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk=None):
        """
            este metodo serve para retornar informacoes do usuario logado e
            so retorna informacao se o id passado por 'i'
        """
        if pk == 'i':
            return response.Response(UserSerializer(request.user,
                                                    context={'request': request}).data)

        return super(UserViewSet, self).retrieve(request, pk)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_fields = ('id', 'name', 'initials',)
    search_fields = ('name', 'initials')

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_fields = ('id','country', 'name', 'uf',)
    search_fields = ('name', 'uf')

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_fields = ('id','state', 'name', )
    search_fields = ('name',)    
    ordering = ('name',)


@api_view(['GET'])
def teste(request):
    if request.method == 'GET':

        print ("Import NFe")
        from sale.import_nfe import ImportNF
        import os
        from django.conf import settings

        nf =ImportNF() 

        filepath = os.path.join(settings.MEDIA_TMP_DIR, 'nfe2.xml')

        a = nf.import_xml(filepath)


        result = dict({
            'success': True,
            'data': a
        })

    return Response(result)    