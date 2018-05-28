# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Census(models.Model):
	age = models.IntegerField()
	workclass = models.CharField(max_length=100)
	fnlwgt = models.IntegerField()
	education = models.CharField(max_length=100)
	education_num = models.IntegerField()
	martial_status = models.CharField(max_length=50)
	occupation = models.CharField(max_length=100)
	relationship = models.CharField(max_length=100)
	race = models.CharField(max_length=20)
	sex = models.CharField(max_length=20)
	capital_gain = models.IntegerField()
	capital_loss = models.IntegerField()
	hours_per_week = models.IntegerField()
	native_country = models.CharField(max_length=50)
	annual_income = models.CharField(max_length=10)

