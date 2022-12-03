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
    if UserInput == None:
       UserInput ="x"
    if StandardInput == None:
       StandardInput ="x"
    results = fuzz.ratio(UserInput.lower(),StandardInput.lower())
    rs = RefinedSoundex()
    ans = rs.distance(UserInput.lower(),StandardInput.lower())
    ans =str(ans)
    results= str(results)
    
    
  
    return JsonResponse({'results':results,'Answer':ans})
# Create your views here.