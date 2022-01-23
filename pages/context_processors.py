from .models import *

def team_pic(request):
    teams = Teams.objects.all()
    return {'teams':teams}#return etmelisen burda yadda saxla burani context proseslerde return etmelisen,ve bunuda templatelerd istifade ede bilersen amma setting.py a qeyd etmelinse TEMPLATE yerine






