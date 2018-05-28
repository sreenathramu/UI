# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.db.models import Count
from django.core import serializers
import json


def getAlldata(request):
	draw = request.GET['draw']
	pageLength = int(request.GET['length'])
	pageNum = int(request.GET['start'])/pageLength + 1
	offset = (pageNum-1) * pageLength
	totalNoRecords = Census.objects.count()
	''' Search Values '''
	relationshipValues = request.GET['columns[7][search][value]']
	raceValues = request.GET['columns[8][search][value]']
	genderValues = request.GET['columns[9][search][value]']
	relationshipValues = [str(x) for x in relationshipValues.split("|") if x]
	raceValues = [str(x) for x in raceValues.split("|") if x]
	genderValues = [str(x) for x in genderValues.split("|") if x]
	censusList = Census.objects.all()
	if relationshipValues:
		censusList = censusList.filter(relationship__in=relationshipValues)
	if raceValues:
		censusList = censusList.filter(race__in=raceValues)
	if genderValues:
		censusList = censusList.filter(sex__in=genderValues)
	recordsFiltered = censusList.count()
	censusList = list(censusList.order_by('id')[offset:offset+pageLength].values())
	return JsonResponse({"draw":draw,"recordsTotal":totalNoRecords,
						 "recordsFiltered":recordsFiltered,
						 "data":json.dumps(censusList)})

def genderDistribution(request):
	distribution = list(Census.objects.values('sex').annotate(y=Count('id')))
	return JsonResponse({'chart':json.dumps(distribution)})

def getRelationshipCount(request):
	relationshipCount = list(Census.objects.values('relationship').annotate(y=Count('id'))
                             .values_list('y',flat=True))
	return JsonResponse({'chart':json.dumps(relationshipCount)})

