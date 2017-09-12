from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        print('Ready for execution')
    return resource(request)

def resource(request):
    return render(request, 'home.html')