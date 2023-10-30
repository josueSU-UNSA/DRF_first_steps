from django.shortcuts import render
from django.http import JsonResponse
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

        return JsonResponse(data_to_return)#Here we return an object so 
                                        # Set safe in False isn't necesary
    elif request.method=='POST':
        #CREATE OPERATION
        serializer=DrinkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

