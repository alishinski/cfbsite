# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Game.game_num_code'
        db.delete_column(u'cfbdata_game', 'game_num_code')

        # Adding field 'Game.num_code'
        db.add_column(u'cfbdata_game', 'num_code',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Game.game_num_code'
        db.add_column(u'cfbdata_game', 'game_num_code',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Game.num_code'
        db.delete_column(u'cfbdata_game', 'num_code')


    models = {
        u'cfbdata.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 19, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_code': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'opponent_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cfbdata.Team']"}),
            'team_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'win': ('django.db.models.fields.NullBooleanField', [], {'default': "'NULL'", 'null': 'True', 'blank': 'True'})
        },
        u'cfbdata.team': {
            'Meta': {'object_name': 'Team'},
            'conference_code': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loss_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mascot_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'school_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'team_num_code': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'win_total': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['cfbdata']