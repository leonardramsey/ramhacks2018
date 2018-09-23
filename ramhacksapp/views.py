# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib

from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers import serialize
from django.template import RequestContext
import urllib

def index(request):
    return render(request, 'miscellaneous/index.html')

def transfer(request):
    if request.method == 'POST':

        sender_address = request.POST.get('sender_address')
        rec_address = request.POST.get('rec_address')
        amount = request.POST.get('amount')
        print(amount)
        dic = {"beneficiary": rec_address, "amount": amount}

        url = "http://35.237.130.214:80/transfer"
        data = urllib.parse.urlencode(dic).encode('utf-8')
        req = urllib.request.Request(url, data=data, method = 'POST')

        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        res = json.loads(resp_json)

        print("before resp")
        print(res)
        print("after resp")
        return JsonResponse(resp_json)
        #return redirect('home')

        #do post logic
        #retrieve form data from html contactForm
        #new post request
        #send request to his api
        #do repsponse logic
        # return to dashbaord
    return render(request, 'miscellaneous/transfer.html')

def dashboard(request):
    # add logic to read from api
    url = ""
    #req = urllib.request.Requst(url, method='GET')
    #resp = urllib.request.urlopen(req).read()#.decode('utf-8)
    data = []
    #for r in resp:
    #    data.append(r)
    return render(request, 'miscellaneous/dashboard.html', {"data":data})
