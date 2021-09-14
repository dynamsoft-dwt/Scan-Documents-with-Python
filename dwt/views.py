from django.http import HttpResponse, request
from django import template
from django.shortcuts import render
import os

# Create your views here.
def index(request):
  return render(request, 'dwt/index.html')