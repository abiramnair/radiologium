# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Module, Track

admin.site.register(Module)
admin.site.register(Track)
# Register your models here.
