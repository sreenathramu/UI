from __future__ import unicode_literals

from django.shortcuts import render
from app.models import Census

def index(request):
	genderList = Census.objects.values('sex').distinct()
	genderList = [str(x['sex']) for x in genderList]
	raceList = Census.objects.values('race').distinct()
	raceList = [str(x['race']) for x in raceList]
	relationshipList = Census.objects.values('relationship').distinct()
	relationshipList = [str(x['relationship']) for x in relationshipList]
	return render(request,'baseTemplate.html',{'gender':genderList,'race':raceList
				,'relationship':relationshipList})