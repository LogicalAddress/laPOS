from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'base/index.html'
    context = {}
    return render(request, template, context)
