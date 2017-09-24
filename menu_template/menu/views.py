from django.shortcuts import render
import requests
import json
# Create your views here.
from django.http import HttpResponse

# Create your views here.
def main(request, url):
    context = {"url":url}
    return render(request, 'menu/main.html', context)