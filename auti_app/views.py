from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.http import JsonResponse

@api_view(['GET'])
def hello_world(request):
    
    solute = request.GET.get('solute')
    
    results = [solute]
    return JsonResponse({'results':solute})

# Create your views here.
