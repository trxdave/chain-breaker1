from django.shortcuts import render

def results(request):
    # Data for results (if any)
    results_data = {
        # Add your context data here
    }
    return render(request, 'results/reporting.html', {"results": results_data})  # Changed to 'reporting.html'
