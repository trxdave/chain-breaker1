from django.shortcuts import render

def resources(request):
    # Example data for the resources page
    resources_data = [
        {
            "title": "National Human Trafficking Hotline",
            "description": "Get immediate help and report trafficking cases.",
            "link": "https://humantraffickinghotline.org"
        },
        {
            "title": "United Nations Office on Drugs and Crime (UNODC)",
            "description": "Learn about global efforts against trafficking.",
            "link": "https://www.unodc.org"
        },
        {
            "title": "Polaris Project",
            "description": "Access in-depth resources on combating human trafficking.",
            "link": "https://polarisproject.org"
        },
        {
            "title": "Freedom Collaborative",
            "description": "A global resource hub for anti-trafficking organizations.",
            "link": "https://freedomcollaborative.org"
        },
    ]
    return render(request, 'resources/resources.html', {"resources": resources_data})
