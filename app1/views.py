from email import message
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    return HttpResponse ('''Congrats''')

@api_view
def firstApi(request):
    message= "API congrats"    
    return Response(message)

# Create your views here.
