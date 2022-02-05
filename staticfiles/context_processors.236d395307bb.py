from .models import *

def team_pic(request):
    teams = Teams.objects.all()
    return {'teams':teams}






