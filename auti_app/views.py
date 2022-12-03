from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.http import JsonResponse
from fuzzywuzzy import fuzz
from pyphonetics import RefinedSoundex

@api_view(['GET'])
def ScoreCalculator(request):
    
    UserInput = request.GET.get('user')
    StandardInput = request.GET.get('standard')
    results = fuzz.ratio(UserInput,StandardInput)
    rs = RefinedSoundex()
    ans = rs.distance(UserInput.lower(),StandardInput.lower())

    return JsonResponse({'results':results,'Answer':ans})

# Create your views here.
