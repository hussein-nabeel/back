from django.shortcuts import render

from django.http import JsonResponse
from .models import Prodect
from .serializers import ProdectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


#get all the drinks 
#serialize them 
#return json
@api_view(['GET','POST'])
def Prodect_list(request,format=None):

 if request.method == 'GET':
    Prodects= Prodect.objects.all()     #get all the drinks 
    serializer = ProdectSerializer(Prodects, many=True)
    return Response(serializer.data)                            #return JsonResponse({'Prodects':serializer.data})

 if request.method == 'POST':
    serializer = ProdectSerializer(data=request.data) 
    if serializer.is_valid() :
        serializer.save ()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view (['GET','PUT','DELETE'])
def Prodect_detail(request,id ,format=None):
    try:
      Prodect =Prodect.objects.get(pk=id)
    except Prodect.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer = ProdectSerializer(Prodect)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
         serializer = ProdectSerializer(Prodect, data=request.data)
         if serializer.is_valid():
            serializer.save ()
            return Response (serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        Prodect.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
      
