from django.shortcuts import render

def results(request):
    return render(request, 'results/results.html')