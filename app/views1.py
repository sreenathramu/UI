# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
# from .serializer import CensusSerializer
#from rest_framework.response import Response
from .models import *
from django.db.models import Count

# Create your views here.

# @csrf_exempt
# @api_view(['GET'])
# def getAlldata(request):
# 	distiribution = CensusSerializer(Census.objects.filter(id=1),many=True)
# 	#return Response(distiribution.data)

# @csrf_exempt
# @api_view(['GET'])
# def genderDistribution(request):
# 	distiribution = Census.objects.values('sex').annotate(Count('id'))
# 	#return Response(distiribution)

def getAlldata(request):
	objects = Census.objects.all()
	return HttpResponse(objects)