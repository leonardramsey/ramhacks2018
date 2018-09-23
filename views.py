# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.core.context_processors import csrf
from django.core import serializers
from django.core.serializers import serialize
from django.template import RequestContext


def index(request):
    return render_to_response('index.html')

