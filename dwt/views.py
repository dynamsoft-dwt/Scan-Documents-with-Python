from django.http import HttpResponse, request
from django import template
from django.shortcuts import render
import os

def index(request):
  return render(request, 'dwt/index.html')

def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['RemoteFile'], str(request.FILES['RemoteFile']))
        return HttpResponse("Successful")

    return HttpResponse("Failed")

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
