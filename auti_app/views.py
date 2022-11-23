from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.http import JsonResponse
from fuzzywuzzy import fuzz

@api_view(['GET'])
def ScoreCalculator(request):
    
    UserInput = request.GET.get('user')
    StandardInput = request.GET.get('standard')
    results = fuzz.partial_ratio(UserInput,StandardInput)
    return JsonResponse({'results':results})

# Create your views here.
