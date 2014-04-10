from django.db import models

import csv
import datetime

from django.db.models.fields import IntegerField
from django.conf import settings

class Conference(models.Model):
    conference_code = models.IntegerField(default=0)
    conference_name = models.CharField(max_length=200)
    subdivision = models.CharField(max_length=200, default="FBS")    

class Team(models.Model):
    #conference = models.ForeignKey(Conference, default=0)
    school_name = models.CharField(max_length=200)
    mascot_name = models.CharField(max_length=200)
    win_total = models.IntegerField(default=0)
    loss_total = models.IntegerField(default=0)
    team_num_code = models.IntegerField(default=0)
    conference_code = models.IntegerField(default=0)   
    def __unicode__(self):
	return self.school_name
	
class Game(models.Model):
    team = models.ForeignKey(Team)
    date = models.DateField(default=datetime.date(2014, 9, 10))
    team_score = models.IntegerField(default=0)
    opponent_score = models.IntegerField(default=0)
    opponent_name = models.CharField(max_length=200, default="opp")
    opponent_code = models.IntegerField(default=0)
    win = models.NullBooleanField(default="NULL")
    num_code = models.CharField(max_length=200) 
