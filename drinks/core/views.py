from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework. decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def drink_list(request):
    
    if request.method=='GET':
        # READ operation
        drink_list_to_serialize=Drink.objects.all()
        drink_serialized=DrinkSerializer(drink_list_to_serialize,many=True)
        data_to_return={
            'drink_list':drink_serialized.data,
        }
        # return JsonResponse(data_to_return,safe=False)

        return Response(data_to_return,status=status.HTTP_200_OK)#Here we return an object so 
                                        # Set safe in False isn't necesary
    elif request.method=='POST':
        #CREATE OPERATION
        serializer=DrinkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def drink_details(request,drink_id):
    drink_to_return=get_object_or_404(Drink,id=drink_id)
    if request.method=='GET':
        
        drink_serialized=DrinkSerializer(drink_to_return,many=False)
        data_to_return={
            'selected_drink':drink_serialized.data,
        }
        return Response(data_to_return,status=status.HTTP_200_OK)

    elif request.method=='PUT':
        drink_serialized=DrinkSerializer(drink_to_return,data=request.data)
        if drink_serialized.is_valid():
            drink_serialized.save()
            return Response(drink_serialized.data,status=status.HTTP_200_OK)

    elif request.method=='DELETE':
        drink_to_return.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        


