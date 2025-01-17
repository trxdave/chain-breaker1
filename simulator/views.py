from django.shortcuts import render
from .models import Scenario

# View to display all scenarios
def simulator_view(request):
    scenarios = Scenario.objects.all()  # Get all scenarios from the database
    return render(request, 'simulator/simulator.html', {'scenarios': scenarios})
