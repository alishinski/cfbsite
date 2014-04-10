from django.contrib import admin
from cfbdata.models import Team
from cfbdata.models import Game
from cfbdata.models import Conference
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    fields = ['team_num_code', 'conference_code']

admin.site.register(Team, TeamAdmin)
admin.site.register(Game)
admin.site.register(Conference)
