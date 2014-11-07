from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context
from django.template.context import RequestContext
from django.http import HttpResponse
from django.template.response import TemplateResponse

def index(request):
    print "hola"
    return TemplateResponse(request, 'index.html', {})


