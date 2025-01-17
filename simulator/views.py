# views.py
from django.shortcuts import render

def simulator(request):
    return render(request, 'simulator/simulator.html')
