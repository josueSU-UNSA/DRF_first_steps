from django.shortcuts import render
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
# Create your views here.

def drink_list(request):
    drink_list_to_serialize=Drink.objects.all()
    drink_serialized=DrinkSerializer(drink_list_to_serialize,many=True)
    return JsonResponse(drink_serialized.data,safe=False)