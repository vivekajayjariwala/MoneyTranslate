from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import FileResponse
from django.http import JsonResponse

def index(request):
    return render(request, 'build/index.html')