from django.shortcuts import render

# This view renders the 'about.html' page
def about_view(request):
    return render(request, 'about/about.html')

# This view renders the 'meettheteam.html' page
def meet_the_team(request):
    return render(request, 'about/meettheteam.html')
