from django.shortcuts import render
from .models import ShinyApp,SfnTeam
from django.conf import settings

# Create your views here.

# index view
def index(request):
    shiny_apps_list = ShinyApp.objects.all()
    return render(request, 'home/index.html', {'list': shiny_apps_list})

# team view
def team(request):
    team_list = SfnTeam.objects.all()
    return render(request, 'home/team.html', {'team_list': team_list})
