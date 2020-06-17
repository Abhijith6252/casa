from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from ajira.models import CmpgInfo
from ajira.serializers import CmpgInfoSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def cmpginfo_list(request):
    
    
    if request.method == 'POST':
        cmpginfo_data = JSONParser().parse(request)
        cmpginfo_serializer = CmpgInfoSerializer(data=cmpginfo_data)
        if cmpginfo_serializer.is_valid():
            cmpginfo_serializer.save()
            return JsonResponse(cmpginfo_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(cmpginfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
