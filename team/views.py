from django.shortcuts import render
from .models import Team


def team_list(request):
    team_obj = Team.objects.all()
    return render(request, 'team-list.html', {'teams': team_obj})
