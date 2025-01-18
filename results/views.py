from django.shortcuts import render

def results(request):
    # Example data for the results page
    results_data = {
        "success_rate": 85,  # Example success rate percentage
        "cases_prevented": 1250,  # Example number of cases prevented
        "user_participation": 420,  # Example number of users who participated
        "top_contributors": [
            {"name": "Global Anti-Trafficking Org", "link": "https://example.org"},
            {"name": "Community Watch", "link": "https://communitywatch.org"},
        ],
        "highlights": [
            "Increased awareness campaigns reached 10,000+ individuals.",
            "Collaboration with local law enforcement led to 50 arrests of traffickers.",
            "Support provided to 300 survivors through rehabilitation programs.",
        ],
    }
    return render(request, 'results/results.html', {"results": results_data})
