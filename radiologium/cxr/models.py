# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from radiologium import settings

class Module(models.Model):
	BEGINNER = 'Beginner'
	INTERMEDIATE = 'Intermediate'
	ADVANCED = 'Advanced'
	SPECIALIST = 'Specialist'
	DIFFICULTY_CHOICES = (
	(BEGINNER, 'Beginner'),
	(INTERMEDIATE, 'Intermediate'),
	(ADVANCED, 'Advanced'),
	(SPECIALIST, 'Specialist'),
	)
	name = models.CharField(max_length=50)
	date_created = models.DateTimeField('date published')
	description = models.TextField(null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	author = models.CharField(max_length=100)
	difficulty = models.CharField(choices=DIFFICULTY_CHOICES, max_length=100)


class Track(models.Model):
	name = models.CharField(max_length=50)
	date_created = models.DateTimeField('date created')
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to=settings.MEDIA_ROOT)


