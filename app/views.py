# pylint: disable=missing-module-docstring
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import stuff_serializer,collection_serializer
from .models import stuff1,collection
from django.shortcuts import get_object_or_404
# Create your views here.


@api_view()
def main_detail(request,id):
    stuff = get_object_or_404(stuff1,pk=id)
    serializer =  stuff_serializer(stuff)
    return Response(serializer.data)



@api_view(['GET' , 'POST'])
def main(request):
    if request.method == "GET":
        set = stuff1.objects.select_related('collector').all()
        serializer =stuff_serializer(set,many=True ,context={"request":request})
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = stuff_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serilozer.validate()
        return Response('hi')


@api_view()   
def collector_path(request,pk):
    return Response('hurrah!')