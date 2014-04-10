from django.shortcuts import render
from django.http import HttpResponse
from cfbdata.models import Team, Game, Conference
from django.template import RequestContext, loader

def index(request):
    constant = "CFB"
    template = loader.get_template('cfbdata/index.html')
    context = RequestContext(request, {
        'constant':constant,
    })
    return HttpResponse(template.render(context))

def teamlist(request):
    team_list = Team.objects.all()
    conference_list = Conference.objects.all()
    template = loader.get_template('cfbdata/teamlist.html')
    context = RequestContext(request, {
        'team_list': team_list,
        'conference_list': conference_list,
    })
    return HttpResponse(template.render(context))

def conference(request, conference_code):
    conf_name = Conference.objects.get(conference_code=conference_code)
    name = conf_name.conference_name
    list = Team.objects.filter(conference_code=conference_code)
    template = loader.get_template('cfbdata/conference.html')
    context = RequestContext(request, {
        'list': list,
        'name': name,
    })
    return HttpResponse(template.render(context))

def team(request, team_num_code, conference_code):
    team = Team.objects.get(team_num_code=team_num_code)
    school_name = team.school_name
    #game_list = team.game_set.all()
    game_list = team.game_set.order_by('-date')
    template = loader.get_template('cfbdata/team.html')
    context = RequestContext(request, {
        'school_name': school_name,
        'game_list': game_list,
    })
    return HttpResponse(template.render(context))

