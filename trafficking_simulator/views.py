from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Render your home template

def about(request):
    return render(request, 'about.html')  # Render your about template

def simulation(request):
    return render(request, 'simulator.html')  # Render your simulation template

def resources(request):
    return render(request, 'resources.html')  # Render your resources template

def results(request):
    return render(request, 'results.html')  # Render your results template
