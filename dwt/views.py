from django.http import HttpResponse, request
from django import template
from django.shortcuts import render
import os

from .models import Image

def index(request):
  return render(request, 'dwt/index.html')

def upload(request):
    if request.method == 'POST':
        # handle_uploaded_file(request.FILES['RemoteFile'], str(request.FILES['RemoteFile']))
        # return HttpResponse("Successful")
        image = Image()
        image.name = request.FILES['RemoteFile'].name
        image.data = request.FILES['RemoteFile']
        image.save()
        return HttpResponse("Successful")

    return HttpResponse("Failed")

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

        return destination
