# Create your views here.
from django.http import HttpResponse
from django import template
from django.template import RequestContext
from django.shortcuts import render

def home(request):
	fp = open('templates/scan.html');
	t = template.Template(fp.read())
	fp.close()
	html = t.render(template.Context({'current_date'}))
	return HttpResponse(html)
